from os import name

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .views import BudgetViewSet, TransactionViewSet

router = DefaultRouter()
router.register('transactions', TransactionViewSet)
router.register('budgets', BudgetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
