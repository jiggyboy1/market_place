from django.shortcuts import render,get_object_or_404
from .cart import Cart
from main.models import Product
from django.http import JsonResponse


# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    context = {'cart_products':cart_products}
    return render(request,'cart_summary.html',context)

def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test for post

    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        #lookup product in database
        product = get_object_or_404(Product,id=product_id)

        # save to a session
        cart.add(product=product)
    
        #let get cart quantity
        cart_quantity = cart.__len__()
        # return a response 
        #response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty':cart_quantity})
        return response


def cart_delete(request):
    pass

def cart_update(request):
    pass