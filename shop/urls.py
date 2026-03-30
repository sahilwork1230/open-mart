from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home' ),
    #Product urls
    path('products/<slug:category_slug>', views.product_view, name = 'product'),
    path('products/product-detail/<str:product_title>/<int:product_id>', views.product_detail, name="product-detail"),
    path('products/product-details/<slug:slug>/', views.product_details, name='product_details'),
    path('address/', views.add_address, name="address"),

    #Auth urls
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name= 'logout'),
    path('profile/', views.profile_view, name='profile'),
    path('order/<int:order_id>/', views.order_detail_view, name='order_detail'),
    path('test/', views.test, name='test'),

    #implementing built-in django auth management for password reset feature
    path("password-reset/", auth_views.PasswordResetView.as_view(
        template_name = "auth/password_reset_form.html",
        email_template_name='auth/password_reset_email.html',
        subject_template_name='auth/password_reset_subject.txt'
    ), name="password_reset"),

    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name='auth/password_reset_done.html'
    ), name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
            template_name='auth/password_reset_confirm.html',
            success_url='/reset/done/'
         ),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='auth/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)