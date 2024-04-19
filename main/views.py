from django.shortcuts import render,redirect
from .models import Product,Cateogry
from django.contrib import messages
from .forms import Register_form
from django.contrib.auth import login,logout,authenticate

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
    try:
        cateogry = Cateogry.objects.get(name=foo)
        product = Product.objects.filter(cateogry=cateogry)
        context = {'product':product,'cateogry':cateogry}
        return render(request,'category_page.html',context)
    except:
        messages.success(request,"That Cateogries Doesn't Exist")
        return redirect('home')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    form = Register_form()
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Your Account Created Succesfully")
            return redirect('home')
    context = {'form':form}
    return render(request,'register.html',context)