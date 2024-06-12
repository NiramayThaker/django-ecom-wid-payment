from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us', views.about_us, name='about-us'),
    path('blog', views.blog, name='blog'),
    path('orders', views.orders, name='orders'),
    path('my-profile', views.my_profile, name='my-profile'),
    path('cart', views.cart, name='cart'),
]
