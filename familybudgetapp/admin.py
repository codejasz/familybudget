from django.contrib import admin
from familybudgetapp.models import Budget, Transaction, Category

# Register your models here.
admin.site.register(Budget)
admin.site.register(Transaction)
admin.site.register(Category)
