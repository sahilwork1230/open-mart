from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Product
from .models import Cart, CartItem
from django.http import JsonResponse


from django.contrib import messages

@login_required(login_url="login")
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if product.stock < 1:
        messages.warning(request, f"{product.title} is currently out of stock.")
        return redirect("product-detail", product_title=product.title, product_id=product.id)

    cart, created = Cart.objects.get_or_create(user = request.user)

    cart_item, item_created = CartItem.objects.get_or_create(
        cart = cart,
        product = product,
        defaults={"price": product.price}
    )

    if not item_created:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
        else:
            messages.warning(request, f"Only {product.stock} units of {product.title} are available.")
            return redirect("cart_detail")

    cart_item.save()
    return redirect("cart_detail")

@login_required(login_url="login")
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, "cart/cart-detail.html", {"cart": cart})


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        cart=request.user.cart
    )
    cart_item.delete()
    return redirect("cart_detail")


@login_required
def increment_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if cart_item.quantity < cart_item.product.stock:
        cart_item.quantity += 1
        cart_item.save()
    else:
        messages.warning(request, f"Only {cart_item.product.stock} units of {cart_item.product.title} are available.")
    return redirect("cart_detail")

@login_required
def decrement_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect("cart_detail")

# AJAX implmentation for cart quantity update
def cart_update(request):
    if request.method == 'POST':
        item_id = request.POST.get("item_id")
        action = request.POST.get("action")
        cart_item = get_object_or_404(CartItem, id= item_id)
        # product = cart_item.product
        if action == 'increment':
            cart_item.quantity += 1
        if action == 'decrement':
            cart_item.quantity -= 1
        cart_item.save()
        return JsonResponse({
            "quantity": cart_item.quantity,
            "total_price": cart_item.quantity * cart_item.product.price
        })

            





