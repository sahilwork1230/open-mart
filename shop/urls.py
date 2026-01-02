from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home' ),
    #Product urls
    path('products/<slug:category_slug>', views.product_view, name = 'product'),
    path('products/product-detail/<str:product_title>/<int:product_id>', views.product_detail, name="product-detail"),
    # path('robots/', views.product_view, name = 'robots'),
    # path('cam/', views.product_view, name = 'cam'),
    # path('spare-parts/', views.product_view, name = 'spare-parts'),

    #Auth urls
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name= 'logout'),
    path('reset-password/', views.reset_password, name="reset-password"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)