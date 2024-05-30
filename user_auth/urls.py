from django.urls import path, include
from . import views 


urlpatterns = [
    path('sign-in', views.sign_in, name='sign-in'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('log-out', views.log_out, name='log-out'),
]

