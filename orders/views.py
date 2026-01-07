from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from django.shortcuts import redirect, get_object_or_404
from cart.models import Cart

# @login_required
# def create_order(request):
#     cart, _ = Cart.objects.get_or_create(user = request.user)

    

#     # Safety check
#     if not cart.items.exists():
#         return redirect("view-cart")
    
#     # Create Order ----- Sahil -----
#     order = Order.objects.create(
#         user = request.user,
#         total_price = cart.total_price()
#     )

#     # Copy cart items in Order object

#     for item in cart.items.all():
#         OrderItem.objects.create(
#             order = order,
#             product_name = item.product.title,
#             price = item.price,
#             quantity = item.quantity
#         )

#     # Clear cart AFTER successful order 
    
#     cart.items.all().delete()
#     return redirect("home")

@login_required
def checkout_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    # safety check
    if not cart.items.exists():
        return redirect("view-cart")
    addresses = request.user.addresses.all()
    return render(
        request,
        'orders/checkout.html',
        {
            "cart": cart,
            "addresses": addresses
        }
    )




