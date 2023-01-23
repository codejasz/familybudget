from django.shortcuts import render
from rest_framework import viewsets, exceptions
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, BudgetSerializer, TransactionSerializer
from .models import User, Budget, Transaction
from .permissions import IsOwnerOrIsPermitted

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()
    permission_classes = [IsOwnerOrIsPermitted]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise exceptions.AuthenticationFailed('Please login to be able to see budget details')
        return self.request.user.budgets.all()


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
