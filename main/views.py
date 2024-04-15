from django.shortcuts import render
from .models import Product,Cateogry


# Create your views here.
def home(request):
    product = Product.objects.all()
    cateogry = Cateogry.objects.all()
    context = {'product':product,'cateogry':cateogry}
    return render(request,'home.html',context)


def review(request,pk):
    room = Product.objects.get(id=pk)
    context = {'room':room}
    return render(request,'product.html',context)

def category(request):
    product = Product.objects.all()
    cateogry = Cateogry.objects.all()
    context = {'product':product,'cateogry':cateogry}
    return render(request,'category.html',context)

def category_page(request,foo):
    cateogry = Cateogry.objects.get(name=foo)
    product = Product.objects.filter(cateogry=cateogry)
    context = {'product':product,'cateogry':cateogry}
    return render(request,'category_page.html',context)