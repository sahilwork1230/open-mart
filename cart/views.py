from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Product
from .models import Cart, CartItem


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user = request.user)

    cart_item, item_created = CartItem.objects.get_or_create(
        cart = cart,
        product = product,
        defaults={"price": product.price}
    )

    if not item_created:
        cart_item.quantity += 1


    cart_item.save()
    return redirect("cart")

@login_required
def view_cart(request):
    pass


