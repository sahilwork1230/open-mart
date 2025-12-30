from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Product

@login_required
def view_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.user.cart
    if cart is not None:
        pass

