from django.urls import path
from . import views


urlpatterns = [
    path('add-to-cart/<int:product_id>',views.add_to_cart, name="add_to_cart"),
    path("view-cart", views.cart_detail, name="cart_detail"),
    path("remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    # path("increment/<int:item_id>/", views.increment_cart_item, name="increment_cart_item"),
    # path("decrement/<int:item_id>/", views.decrement_cart_item, name="decrement_cart_item"),
    # AJAX implementation for cart quantity updates

    path('cart/update/',views.cart_update, name='cart_update'),
]