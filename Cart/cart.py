from Booking.models import Item

class Cart():
    def __init__(self, request):
        self.session = request.session

        #Get session key if it Exists
        cart = self.session.get('session_key')

        #Create session key if it Doesn't Exists
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #make cart avalibale
        self.cart = cart

    def add(self, item):
        item_id = str(item.id)

        if item_id in self.cart:
            pass
        else:
            self.cart[item_id] = {'Period': str(item.period)}

        self.session.modified = True

    def get_items(self):
        item_ids = self.cart.keys()
        items=Item.objects.filter(id__in=item_ids)
        return items
    
    def delete(self, item):
        item_id = str(item)
        # Delete from dictionary/cart
        if item_id in self.cart:
            del self.cart[item_id]
        
        self.session.modified = True
    
    #cart item Counter for badge
    def __len__(self):
	    return len(self.cart)
