from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import TokenGenerator, generate_token

# Create your views here.
def sign_in(request):
    context = {"load_form": "log-in", "title": "Log In"}
    return render(request, 'auth/reg_forms.html', context=context)


def sign_up(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf-password']

        if password == conf_password:
            if User.objects.filter(email=email).exists():
                messages.warning(request, "This email is already been used")
                return redirect('sign-up')
                # return HttpResponse("This email is already been used")
            else:
                user = User(username=email, email=email, password=password)
                user.is_active = False
                user.save()
                email_subject = "Activate Your Account"
                message = render_to_string('activate.html', {
                    'user': user,
                    'domain': '127.0.0.1:8000',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': generate_token.make_token(user)
                })
                messages.success(request, "User Created Successfully")
                return redirect('sign-up')
                # return HttpResponse("user created")
        else:
            messages.warning(request, "Password doesn't match")
            return redirect('sign-up')
            # return HttpResponse("Password doesn't match")      
    else:
        context = {"load_form": "sign-up", "title": "Sign Up"}
        return render(request, 'auth/reg_forms.html', context=context)


def log_out(request):
    logout(request)
    return redirect("home")
