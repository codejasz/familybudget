from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Budget, Transaction, User
from .permissions import IsOwnerOrIsPermitted, IsOwner
from .serializers import (
    BudgetSerializer,
    SharedSerializer,
    TransactionSerializer,
    UserSerializer,
)


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [IsOwnerOrIsPermitted]

    def get_queryset(self):
        user_budgets = self.request.user.budgets.all()
        user_budgets_permitted = Budget.objects.filter(
            shared_with__shared_with=self.request.user
        )
        return user_budgets | user_budgets_permitted


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrIsPermitted]


class SharedViewSet(viewsets.ModelViewSet):
    serializer_class = SharedSerializer
    queryset = Transaction.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
