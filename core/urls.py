from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us', views.about_us, name='about-us'),
    path('blog', views.blog, name='blog'),
    path('orders', views.orders, name='orders'),
    path('my-profile', views.my_profile, name='my-profile'),
    path('cart', views.view_cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('add-item', views.add_item, name='add-item'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear-cart/', views.clear_cart, name='clear_cart'),
    path('view-product/<int:product_id>/', views.view_product, name='view_product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
