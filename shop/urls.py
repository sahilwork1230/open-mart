from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name = 'home' ),
    path('cart/', views.cart, name="cart"),
    #Product urls
    path('drones/', views.product_view, name = 'drones'),
    path('robots/', views.product_view, name = 'robots'),
    path('cam/', views.product_view, name = 'cam'),
    path('spare-parts/', views.product_view, name = 'spare-parts'),

    #Auth urls
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name= 'logout'),
    path('reset-password/', views.reset_password, name="reset-password"),

]