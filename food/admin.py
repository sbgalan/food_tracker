from django.contrib import admin

# Register your models here.
from .models import Food, Meal #classes from models

admin.site.register(Food)
admin.site.register(Meal)
