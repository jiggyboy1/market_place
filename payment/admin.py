from django.contrib import admin
from .models import ShippingAddress,Order,OrderItems
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItems)


#create other orderitems inline

class OrderItemInline(admin.StackedInline):
    model = OrderItems
    extra = 0

#Extend our order model

class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ["date_ordered"]
    inlines = [OrderItemInline]


admin.site.unregister(Order)


admin.site.register(Order,OrderAdmin)