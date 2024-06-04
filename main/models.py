from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save

# Create your models here.

class Cateogry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"
    

class Product(models.Model):
    name = models.CharField(max_length=150)
    cateogry = models.ForeignKey(Cateogry,on_delete=models.CASCADE)
    price = models.DecimalField(default=0 , decimal_places=2,max_digits =12)
    description = models.CharField(max_length=200, null=True,blank=True)
    image = models.ImageField(upload_to='photo/')
    flash_sale = models.BooleanField(null=True,default=True)

    def __str__(self) -> str:
        return f"{self.description[0:30]}"
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User,auto_now=True)
    phone =models.CharField(max_length=25,blank=True)
    address1 = models.CharField(max_length=205,blank=True)
    address2 = models.CharField(max_length=25,blank=True)
    city =  models.CharField(max_length=25,blank=True)
    country = models.CharField(max_length=25,blank=True)
    image = models.ImageField(upload_to='profile/',blank=True,null=True)

    def __str__(self) -> str:
        return f'{self.user.username}'
    
def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile,sender=User)


class Customer(models.Model):
    first_name =models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length = 100, default='',blank=True)
    phone = models.CharField(max_length=20,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.product
     
class Review(models.Model):
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    body = models.CharField(max_length=300,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.host} {self.product}"
    