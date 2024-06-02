from django.shortcuts import render, HttpResponse

# Create your views here.
def sign_in(request):
    return render(request, 'about_us.html')
    


def sign_up(request):
    return render(request, 'auth/sign_up.html')


def log_out(request):
    return HttpResponse("Log out")
