from django.db import models
from django.contrib.auth.models import User
from .managers import BudgetManager
from .constants import TRANSACTION_CHOICES

class Budget(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    objects = BudgetManager()

    def get_balance(self) -> int:
        balance = BudgetManager.calculate_balance(self)
        return balance

    def __str__(self) -> str:
        return f'{self.get_balance():.2f}'


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Transaction(models.Model):
    description = models.CharField(max_length=255, blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=2, blank=False, null=False, choices=TRANSACTION_CHOICES)
    created_at = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transactions')

    def __str__(self) -> str:
        return f'{self.transaction_type} - {self.description}: {self.amount}'


class Shared(models.Model):
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
