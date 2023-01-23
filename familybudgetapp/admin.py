from django.contrib import admin

from familybudgetapp.models import Budget, Category, Shared, Transaction

# Register your models here.
admin.site.register(Budget)
admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(Shared)
