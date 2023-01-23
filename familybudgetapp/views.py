from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Budget, Transaction, User
from .permissions import IsOwnerOrIsPermitted
from .serializers import (BudgetSerializer, TransactionSerializer,
                          UserSerializer)


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
