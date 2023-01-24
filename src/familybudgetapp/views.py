from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .models import Budget, Transaction, User
from .permissions import IsOwner, IsOwnerOrIsPermitted
from .serializers import (BudgetSerializer, SharedSerializer,
                          TransactionSerializer, UserSerializer)


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = UserSerializer
    queryset = User.objects.all()

class BudgetViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsOwnerOrIsPermitted]

    serializer_class = BudgetSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_budgets = self.request.user.budgets.all()
            user_budgets_permitted = Budget.objects.filter(
                shared_with__shared_with=self.request.user
            )
            return user_budgets | user_budgets_permitted
        else:
            raise PermissionDenied('You don\'t have permission to access this page') 

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class SharedViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
 
    serializer_class = SharedSerializer
    queryset = Transaction.objects.all()
