from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Budget, Transaction, User
from .permissions import IsOwnerOrIsPermitted, IsOwner
from .serializers import (BudgetSerializer, SharedSerializer,
                          TransactionSerializer, UserSerializer)


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()
    permission_classes = [IsOwnerOrIsPermitted]


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = [IsAuthenticated]


class SharedViewSet(viewsets.ModelViewSet):
    serializer_class = SharedSerializer
    queryset = Transaction.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
