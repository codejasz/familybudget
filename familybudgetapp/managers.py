from django.db.models import Manager, Sum

from .constants import EXPENSE, INCOME


class BudgetManager(Manager):
    def calculate_incomes(self) -> int:
        total_incomes = self.transactions.filter(transaction_type=INCOME).aggregate(
            amount=Sum("amount", default=0)
        )
        return int(total_incomes['amount'])

    def calculate_expenses(self) -> int:
        total_expenses = self.transactions.filter(transaction_type=EXPENSE).aggregate(
            amount=Sum("amount", default=0)
        )
        return int(total_expenses['amount'])

    def calculate_balance(self) -> int:
        """Dynamically calculate budget balance. Returns int to avoid floating point issue"""
        total_incomes = self.transactions.filter(transaction_type=INCOME).aggregate(
            amount=Sum("amount", default=0)
        )
        total_expenses = self.transactions.filter(transaction_type=EXPENSE).aggregate(
            amount=Sum("amount", default=0)
        )
        return int(total_incomes['amount'] - total_expenses['amount'])

    def calculate_balance_by_category(self, category: str) -> int:
        total_amount = self.transactions.filter(category__name=category).aggregate(
            amount=Sum("amount", default=0)
        )
        return int(total_amount['amount'])
