from django.contrib import admin

# Register your models here.
from .models import Salaries,Employees

admin.site.register(Salaries)
admin.site.register(Employees)