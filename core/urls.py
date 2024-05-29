from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us', views.contact_us, name='contact-us'),
    path('about-us', views.about_us, name='about-us'),
    path('sign-in', views.sign_in, name='sign-in'),
]
