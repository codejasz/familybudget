from rest_framework.test import APITestCase

from .constants import EXPENSE, INCOME
from .factories import (BudgetFactory, CategoryFactory, TransactionFactory,
                        UserFactory)
from .managers import BudgetManager


class TestBudgetModel(APITestCase):
    def setUp(self):
        self.owner = UserFactory()
        self.budget = BudgetFactory(owner=self.owner)

        # create incomes with total of 100
        TransactionFactory(
            budget=self.budget,
            description='test1',
            amount=10,
            transaction_type='IN',
            category=CategoryFactory(name='CAT1'),
        )
        TransactionFactory(
            budget=self.budget,
            description='test2',
            amount=30,
            transaction_type='IN',
            category=CategoryFactory(name='CAT1'),
        )
        TransactionFactory(
            budget=self.budget, description='test3', amount=60, transaction_type=INCOME
        )

        # create expenses with total of 60
        TransactionFactory(
            budget=self.budget,
            description='test1',
            amount=10,
            transaction_type='EX',
            category=CategoryFactory(name='CAT2'),
        )
        TransactionFactory(
            budget=self.budget,
            description='test2',
            amount=20,
            transaction_type='EX',
            category=CategoryFactory(name='CAT2'),
        )
        TransactionFactory(
            budget=self.budget, description='test3', amount=30, transaction_type=EXPENSE
        )

    def test_incomes_sum(self):
        self.assertEqual(BudgetManager.calculate_incomes(self.budget), 100)

    def test_expenses_sum(self):
        self.assertEqual(BudgetManager.calculate_expenses(self.budget), 60)

    def test_balance_sum(self):
        self.assertEqual(BudgetManager.calculate_balance(self.budget), 40)

    def test_incomes_by_category(self):
        self.assertEqual(BudgetManager.calculate_balance_by_category(self.budget, category='CAT1'), 40)

    def test_expenses_by_category(self):
        self.assertEqual(BudgetManager.calculate_balance_by_category(self.budget, category='CAT2'), 30)

# class TestBudgetPermision(APITestCase):
#     def setUp(self):
#         self.owner = UserFactory()
