from django.contrib import admin

# Register your models here.
from shop.models import category,product

admin.site.register(category)
admin.site.register(product)