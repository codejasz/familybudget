from django.contrib.auth.models import User
from .models import Budget
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email', 'groups']

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
