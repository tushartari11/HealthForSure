from home.models import Medicine

class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('sessionkey')

        if 'sessionkey' not in request.session:
            cart = self.session['sessionkey'] = {}

        self.cart = cart

    def add(self,  medicine, dosage, quantity):

        product_id = str(medicine.id)
        product_dosage = str(dosage)
        product_quantity = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = [product_dosage, int(product_quantity)]

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Medicine.objects.filter(id__in=product_ids)
        return products
    
    def get_dandqs(self):
        dandqs = self.cart
        return dandqs
    
    def get_total(self):
        product_ids = self.cart.keys()
        products = Medicine.objects.filter(id__in=product_ids)
        dandqs = self.cart
        total = 0
        for key, value in dandqs.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    total = total + ( product.price * value[1] )
        return total
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True