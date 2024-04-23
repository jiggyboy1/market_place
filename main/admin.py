from django.contrib import admin
from .models import Product,Profile,Cateogry,Customer,Review
# Register your models here.


admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Cateogry)
admin.site.register(Customer)
admin.site.register(Review)