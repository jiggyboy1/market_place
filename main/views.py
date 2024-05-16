from django.shortcuts import render,redirect
from .models import Product,Cateogry,Review
from django.contrib import messages
from .forms import Register_form,Updateuserform,ChangePasswordForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    product = Product.objects.all()
    cateogry = Cateogry.objects.all()
    context = {'product':product,'cateogry':cateogry}
    return render(request,'home.html',context)


def review(request,pk):
    room = Product.objects.get(id=pk)
    message = room.review_set.all().order_by('-created')
    room_count = room.review_set.count()

    if request.method == 'POST':
        if request.user.is_authenticated:
            pass
        else:
            messages.error(request,'You must be logged in')
            return redirect('home')
        message1 = Review.objects.create(
            host = request.user,
            product = room,
            body = request.POST.get('message'),
        )
        room.review_set.add()
        return redirect('product',pk=room.id)
    
    context = {'room':room,'message':message,'room_count':room_count}
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
            messages.success(request,'You have logged in')
            return redirect('home')
        else:
            messages.error(request,"Your Username or Password Are Incorrect")
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
            user=form.save()
            login(request,user)
            messages.success(request,"Your Account Created Succesfully")
            return redirect('home')
        else:
            for error in list(form.errors.values()):
                messages.error(request,error)
    context = {'form':form}
    return render(request,'register.html',context)


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = Updateuserform(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request,current_user)
            messages.success(request,"User Has Been Updated")
            return redirect('home')
        context = {'user_form':user_form}
        return render(request,'update_user.html',context)
    else:
        messages.success(request,'You Must Be Logged In To Access This Page')
        return redirect('home')
    
def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user,request.POST)
            
            if form.is_valid():
                form.save()
                messages.success(request,"Your Password Has Been Updated, Please Log In Again....")
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request,error)
                    return redirect('update_password')

        else:
            form = ChangePasswordForm(current_user)
            context = {'form':form}
            return render(request,'update_password.html',context)
        
    else:
        messages.success(request,'You Must Be Logged In')
        return redirect('home')

def update_info(request):
    pass