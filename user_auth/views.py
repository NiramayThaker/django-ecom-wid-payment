from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import TokenGenerator, generate_token
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic import View
from .forms import RegistrationForm


# Create your views here.
def sign_in(request):
	if request.method == "POST":
		email = request.POST['email']
		passwd = request.POST['password']
		my_user = authenticate(username=email, password=passwd)

		if my_user is not None:
			login(request, my_user)
			return redirect('home')
		else:
			messages.error(request, 'Something went wrong')

	context = {"load_form": "log-in", "title": "Log In"}
	return render(request, 'auth/reg_forms.html', context=context)


def sign_up(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('sign-in')

	context = {"load_form": "sign-up", "title": "Sign Up", 'form': form}
	return render(request, 'auth/reg_forms.html', context=context)


def log_out(request):
	logout(request)
	return redirect("home")


class ActivateAccountView(View):
	def get(self, request, uidb64, token):
		try:
			uid = force_str(urlsafe_base64_decode(uidb64))
			user = User.objects.get(pk=uid)
		except Exception as ex:
			user = None

		if user is not None and generate_token.check_token((user, token)):
			user.is_active = True
			user.save()
			messages.info(request, "Account Activated Successfully")
			return redirect('sign-in')

		return render(request, 'auth/activation_fail.html')
