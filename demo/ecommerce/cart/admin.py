from django.contrib import admin

# Register your models here.
from cart.models import cart
from cart.models import Order
from cart.models import Account

admin.site.register(cart)
admin.site.register(Order)
admin.site.register(Account)