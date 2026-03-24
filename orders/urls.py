from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout_view, name="checkout" ),
    path('payment/', views.place_order, name = "place_order"),
]