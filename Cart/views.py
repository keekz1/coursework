from django.shortcuts import render, get_object_or_404
from .cart import Cart
from Booking.models import Item
from django.http import JsonResponse
from django.contrib import messages



def historicalindex(request):
    return render(request, 'historicalIndex.html')

def cart_summary(request):
    cart = Cart(request)
    cart_items = cart.get_items
    return render(request, 'Cartpage.html',{"cart_items":cart_items})



def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        
        item_id = int(request.POST.get('item_id'))
        
        item = get_object_or_404(Item, id=item_id)

        cart.add(item=item)

        # Get Cart Quantity
        cart_quantity = cart.__len__()

        # response = JsonResponse({'Item Name: ': item.name})
        response = JsonResponse({'qty': cart_quantity})
        return response
    



def cart_delete(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		item_id = int(request.POST.get('item_id'))
		# Call delete Function in Cart
		cart.delete(item=item_id)

		response = JsonResponse({'item':item_id})
		messages.success(request, ("Item Deleted From Shopping Cart..."))
		return response
