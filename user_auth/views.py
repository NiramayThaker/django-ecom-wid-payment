from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User

# Create your views here.
def sign_in(request):


    return render(request, 'log_in.html')


def sign_up(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf-password']

        if password == conf_password:
            if User.objects.filter(email=email).exists():
                return HttpResponse("This email is already been used")
            else:
                user = User(username=email, email=email, password=password)
                user.save()
                # return redirect('sign-in')
                return HttpResponse("user created")
        else:
            return HttpResponse("Password doesn't match")            
    else:
        return render(request, 'sign_up.html')


def log_out(request):
    return HttpResponse("Log out")
