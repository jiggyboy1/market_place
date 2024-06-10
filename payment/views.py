from django.shortcuts import render,redirect
from cart.cart import Cart
from payment.forms import ShippingForm
from .models import ShippingAddress,Order,OrderItems
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import Profile,Product
from django.contrib.auth.models import User

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
    return render(request,'payment/payment_success.html')

def process_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()

        my_shipping = request.session.get('my_shipping')

        full_name = my_shipping['shipping_full_name']
        email = my_shipping['shipping_email']
        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_full_name']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_country']}\n{my_shipping['shipping_email']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}"
        amount_paid = totals


        #create order

        if request.user.is_authenticated:
            user = request.user

            create_order = Order.objects.create(
                user = user,
                full_name = full_name,
                shipping_address = shipping_address,
                email = email,
                amount_paid = amount_paid
            )
            create_order.save()

            order_id = create_order.pk
            # get product id 
            for product in cart_products():
                product_id = product.id
                if product.flash_sale:
                    price = product.price
                else:
                    price = product.price

                # get quantity
                for key,value in quantities().items():
                    if int(key) == product.id:
                        # create order items
                        create_order_item = OrderItems(
                            order_id = order_id,
                            product_id = product_id,
                            user = user,
                            quantity =value ,
                            price = price,
                        )
                        create_order_item.save()
            #delete our cart 
            for key in list(request.session.keys()):
                if key == "session_key":
                    #delete key 
                    del request.session[key]

            messages.success(request,"Order Create")
            
            

        context = {'cart_products':cart_products,'quantities':quantities,'totals':totals, 'shipping_info':my_shipping}
        return render(request,'payment/process_order.html',context)
    else: 
        return redirect('home')