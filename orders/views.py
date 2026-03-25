from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from django.shortcuts import redirect, get_object_or_404
from cart.models import Cart
from shop.utils.indian_states import INDIAN_STATES
from shop.models import Address
from django.contrib import messages

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

@login_required(login_url='login')
def checkout_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    # safety check
    if not cart.items.exists():
        return redirect("view-cart")
    addresses = request.user.addresses.all()
    return render(
        request,
        'order/checkout.html',
        {
            "cart": cart,
            "addresses": addresses,
            "states": INDIAN_STATES
        }
    )

from django.db import transaction

@login_required(login_url='login')
def place_order(request):
    address_id = request.POST.get("address")
    cart = get_object_or_404(Cart, user=request.user)
    address = Address.objects.get(id=address_id, user=request.user)
    
    address_snapshot = f"{address.name}\n{address.full_address}"
    
    with transaction.atomic():
        # First, verify stock for all items
        for item in cart.items.all():
            if item.product.stock < item.quantity:
                messages.error(request, f"Sorry, {item.product.title} just went out of stock or has insufficient quantity.")
                return redirect("cart_detail")
        
        # If all items are in stock, create the order and decrement stock
        new_order_instance = Order.objects.create(
            user=request.user,
            address=address,
            address_snapshot=address_snapshot,
            total_price=cart.total_price(),
            is_paid=True,
        )
        
        for item in cart.items.all():
            # Create OrderItem
            OrderItem.objects.create(
                order=new_order_instance,
                product_name=item.product.title,
                price=item.price,
                quantity=item.quantity
            )
            # Decrement Stock
            product = item.product
            product.stock -= item.quantity
            product.save()

        # Clear cart AFTER successful order 
        cart.items.all().delete()

    return render(request, 'order/order_success.html')






