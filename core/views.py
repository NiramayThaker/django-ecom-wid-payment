from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')


def contact_us(request):
    return render(request, 'contact_us.html')


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

