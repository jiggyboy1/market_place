from django.contrib import admin
from .models import ShippingAddress,Order,OrderItems
# Register your models here.

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItems)