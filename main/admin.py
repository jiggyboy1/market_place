from django.contrib import admin
from .models import Product,Profile,Cateogry,Customer,Review
from django.contrib.auth.models import User
# Register your models here.


admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Cateogry)
admin.site.register(Customer)
admin.site.register(Review)


#mix profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile


#extend User model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username','first_name','last_name','email']
    inlines = [ProfileInline]

admin.site.unregister(User)

admin.site.register(User,UserAdmin)