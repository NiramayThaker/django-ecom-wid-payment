from django.shortcuts import render

# Create your views here.
def sign_in(request):
    return render(request, 'auth/sign_in.html')


def sign_up(request):
    return render(request, 'auth/sign_up.html')


def log_out(request):
    return render(request, 'auth/log_out.html')