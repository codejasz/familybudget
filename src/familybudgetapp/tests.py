from rest_framework.test import APITestCase

from .constants import EXPENSE, INCOME
from .factories import BudgetFactory, CategoryFactory, TransactionFactory, UserFactory
from .managers import BudgetManager


class TestBudgetModel(APITestCase):
    def setUp(self):
        self.owner = UserFactory()
        self.budget = BudgetFactory(owner=self.owner)
        self.category1 = CategoryFactory()
        self.category2 = CategoryFactory()

        # create incomes with total of 100
        TransactionFactory(
            budget=self.budget,
            amount=10,
            transaction_type=INCOME,
            category=self.category1,
        )
        TransactionFactory(
            budget=self.budget,
            amount=30,
            transaction_type=INCOME,
            category=self.category1,
        )
        TransactionFactory(budget=self.budget, amount=60, transaction_type=INCOME)

        # create expenses with total of 60
        TransactionFactory(
            budget=self.budget,
            amount=10,
            transaction_type=EXPENSE,
            category=self.category2,
        )
        TransactionFactory(
            budget=self.budget,
            amount=20,
            transaction_type=EXPENSE,
            category=self.category2,
        )
        TransactionFactory(budget=self.budget, amount=30, transaction_type=EXPENSE)

    def test_incomes_sum(self):
        self.assertEqual(BudgetManager.calculate_incomes(self.budget), 100)

    def test_expenses_sum(self):
        self.assertEqual(BudgetManager.calculate_expenses(self.budget), 60)

    def test_balance_sum(self):
        self.assertEqual(BudgetManager.calculate_balance(self.budget), 40)

    def test_incomes_by_category(self):
        self.assertEqual(
            BudgetManager.calculate_balance_by_category(
                self.budget, category=self.category1.name
            ),
            40,
        )

    def test_expenses_by_category(self):
        self.assertEqual(
            BudgetManager.calculate_balance_by_category(
                self.budget, category=self.category2.name
            ),
            30,
        )
