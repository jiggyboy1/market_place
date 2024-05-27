from django.shortcuts import render,redirect
from cart.cart import Cart
from payment.forms import ShippingForm
from .models import ShippingAddress
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.



def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()

        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping

        
        if request.user.is_authenticated:
            shipping_form = request.POST
            context = {'cart_products':cart_products,'quantities':quantities,'totals':totals, 'shipping_info':request.POST}
            return render(request,'payment/billing_info.html',context)
        else:
            pass



            shipping_form = request.POST
            context = {'cart_products':cart_products,'quantities':quantities,'totals':totals, 'shipping_info':request.POST}
            return render(request,'payment/billing_info.html',context)
    else:
        messages.success(request,"You Need To Login In Order To Continue")
        return redirect('home')



    
@login_required(login_url='login')
def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user=request.user)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        context = {'cart_products':cart_products,'quantities':quantities,'totals':totals, 'shipping_form':shipping_form}
        return render(request,'payment/checkout.html',context)


    else:
        messages.success(request,"You Need To Login In Order To Continue")
        return redirect('login')



def payment_success(request):
    messages.success(request,"Payment Successful")
    return render(request,'payment/payment_success.html',)