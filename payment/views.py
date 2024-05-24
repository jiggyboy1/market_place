from django.shortcuts import render,redirect
from cart.cart import Cart
from payment.forms import ShippingForm
from .models import ShippingAddress
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
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
    return render(request,'payment/payment_success.html',)