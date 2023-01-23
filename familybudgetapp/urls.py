from os import name
from django.urls import path, include

from . import views
from .views import BudgetViewSet, TransactionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('transactions', TransactionViewSet)
router.register('budgets', BudgetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
