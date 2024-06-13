from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    all_products = Product.objects.all()
    context = {'products': all_products}
    print(f"\n\n\n\n\n{all_products}\n\n\n\n")
    return render(request, 'index.html', context=context)


def about_us(request):
    return render(request, 'log_in.html')


def blog(request):
    pass


def orders(request):
    pass


def my_profile(request):
    pass


def cart(request):
    pass

