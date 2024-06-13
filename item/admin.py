from django.contrib import admin

# Register your models here.
from .models import Category, Item
# we can use .models as this file is in the same directory

admin.site.register(Category)
admin.site.register(Item)
