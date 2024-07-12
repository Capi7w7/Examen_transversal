from decimal import Decimal
from django.conf import settings
from repuestos.models import Repuesto

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, repuesto, quantity=1, override_quantity=False):
        repuesto_id = str(repuesto.id)
        if repuesto_id not in self.cart:
            self.cart[repuesto_id] = {'quantity': 0, 'price': str(repuesto.precio)}
        if override_quantity:
            self.cart[repuesto_id]['quantity'] = quantity
        else:
            self.cart[repuesto_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, repuesto, quantity=1):
        repuesto_id = str(repuesto.id)
        if repuesto_id in self.cart:
            if self.cart[repuesto_id]['quantity'] > quantity:
                self.cart[repuesto_id]['quantity'] -= quantity
            else:
                del self.cart[repuesto_id]
            self.save()

    def __iter__(self):
        repuesto_ids = self.cart.keys()
        repuestos = Repuesto.objects.filter(id__in=repuesto_ids)
        cart = self.cart.copy()
        for repuesto in repuestos:
            cart[str(repuesto.id)]['repuesto'] = repuesto
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()