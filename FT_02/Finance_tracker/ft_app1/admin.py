from django.contrib import admin
from .models import Profile,Income,Expense
# Register your models here.


admin.site.register(Profile)
admin.site.register(Income)
admin.site.register(Expense)