from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def about_us(request):
    return render(request, 'about_us.html')


def sign_in(request):
    return render(request, 'sign-in.html')