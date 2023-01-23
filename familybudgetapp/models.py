from django.contrib.auth.models import User
from django.db import models

from .constants import TRANSACTION_CHOICES
from .managers import BudgetManager


class Budget(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    objects = BudgetManager()

    # def __str__(self) -> str:
    #     return f'{self.get_balance():.2f}'


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Transaction(models.Model):
    description = models.CharField(max_length=255, blank=False, null=False)
    amount = models.IntegerField()
    transaction_type = models.CharField(
        max_length=2, blank=False, null=False, choices=TRANSACTION_CHOICES
    )
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category'
    )
    budget = models.ForeignKey(
        Budget, on_delete=models.CASCADE, related_name='transactions'
    )

    def __str__(self) -> str:
        return f'{self.transaction_type} - {self.description}: {self.amount:.2f}'


class Shared(models.Model):
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
