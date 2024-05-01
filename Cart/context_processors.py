from .cart import Cart

# create contact for processor for all page integration
def cart(request):

    return {'cart':Cart(request)}