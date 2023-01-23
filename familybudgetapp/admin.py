from django.contrib import admin
from familybudgetapp.models import Budget, Income, Expense, Category

# Register your models here.
admin.site.register(Budget)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Category)
