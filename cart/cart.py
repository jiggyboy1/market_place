from main.models import Product
class Cart():
    def __init__(self,request) -> None:
        self.session = request.session

        cart = self.session.get('session_key')

        #if the user is new, no session key! create one

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #make sure cart is available on all pages of site

        self.cart = cart

    def add(self,product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        # logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price':str( product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True 

    def cart_total(self):
        #get prods ids
        product_ids = self.cart.keys()
        #lookup those keys in our product database model
        products = Product.objects.filter(id__in=product_ids)

        quantities = self.cart
        #start counting at 0
        total = 0
        for key , value in quantities.items():
            # convert key string into int so we can math
            key = int(key)
            for product in products:
                if product.id == key:
                    total = total + (product.price * int(value))

        return total
    


    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # get ids from cart
        product_ids = self.cart.keys()
        # use ids to lookup prods in database model
        products = Product.objects.filter(id__in=product_ids)

        #return those looked up products
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self,product,quantity):
        product_id = str(product)
        product_qty = str(quantity)

        #get the cart
        ourcart = self.cart
        #update dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True
        thing = self.cart
        return thing
    
    def delete(self,product):
        product_id = str(product)
        #delete from dictionar/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True