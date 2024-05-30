from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us', views.contact_us, name='contact-us'),
    path('about-us', views.about_us, name='about-us'),
    path('sign-in', views.sign_in, name='sign-in'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('blog', views.blog, name='blog'),
    path('orders', views.orders, name='orders'),
    path('my-profile', views.my_profile, name='my-profile'),
    path('cart', views.cart, name='cart'),
]
