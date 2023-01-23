from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Budget, Transaction


class UserSerializer(serializers.ModelSerializer):
    budgets = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='budget-detail'
    )

    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'budgets']


class BudgetSerializer(serializers.ModelSerializer):
    transactions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Budget
        fields = ['name', 'description', 'owner', 'transactions']


class TransactionSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Transaction
        fields = [
            'description',
            'amount',
            'transaction_type',
            'created_at',
            'category',
            'budget',
        ]
