import factory
from django.contrib.auth.models import User

from .models import Budget, Category, Transaction


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: "User_%03d" % n)
    first_name = factory.Sequence(lambda n: "User %03d" % n)
    email = factory.Sequence(lambda n: "user_%03d@example.com" % n)

    class Meta:
        model = User


class BudgetFactory(factory.django.DjangoModelFactory):
    name = 'example budget'
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = Budget


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f'Category {n}')

    class Meta:
        model = Category


class TransactionFactory(factory.django.DjangoModelFactory):
    description = factory.Sequence(lambda n: f'Transaction {n}')
    category = factory.SubFactory(CategoryFactory)
    budget = factory.SubFactory(BudgetFactory)

    class Meta:
        model = Transaction
