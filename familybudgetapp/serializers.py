from django.contrib.auth.models import User
from .models import Budget, Transaction
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    budgets = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='budget-detail'
    )
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'budgets']


class BudgetSerializer(serializers.ModelSerializer):
    transactions = serializers.StringRelatedField(many=True)
    class Meta:
        model = Budget
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True)
    class Meta:
        model = Transaction
        fields = '__all__'