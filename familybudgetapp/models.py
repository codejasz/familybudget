from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.functions import Coalesce


class BudgetManager(models.Manager):
    def calculate_balance(self) -> float:
        """Dynamically calculate budget balance"""
        total_incomes = self.incomes.aggregate(amount=models.Sum("amount", default=0.0))
        total_expenses = self.expenses.aggregate(amount=models.Sum("amount", default=0.0))
        return float(total_incomes["amount"] - total_expenses["amount"])


class Budget(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = BudgetManager()

    def get_balance(self) -> float:
        balance = BudgetManager.calculate_balance(self)
        return balance

    def __str__(self) -> str:
        return f"{self.get_balance()}"


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Income(models.Model):
    description = models.CharField(max_length=255, blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="incomes")

    def __str__(self) -> str:
        return f"{self.description}: {self.amount}"


class Expense(models.Model):
    description = models.CharField(max_length=255, blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    budget = models.ForeignKey(
        Budget, on_delete=models.CASCADE, related_name="expenses"
    )

    def __str__(self) -> str:
        return f"{self.description}: {self.amount}"
