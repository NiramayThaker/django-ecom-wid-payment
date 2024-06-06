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


# Create your views here.
def sign_in(request):
	if request.method == "POST":
		email = request.POST['email']
		passwd = request.POST['password']

		print(f"\n\n\n\n\n\n\n {email} - {passwd} \n\n\n\n\n\n\n")

		# my_user = User.objects.get(username=email, password=passwd)
		my_user = authenticate(username=email, password=passwd)
		print(f"\n\n\n\n\n\n\n {my_user} \n\n\n\n\n\n\n")

		if my_user is not None:
			login(request, my_user)
			return redirect('home')
		else:
			messages.error(request, 'Something went wrong')

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
			else:
				user = User(username=email, email=email, password=password)
				user.save()

				# user.is_active = False
				# email_subject = "Activate Your Account"
				# message = render_to_string('auth/activate.html', {
				# 	'user': user.username,
				# 	'domain': get_current_site(request).domain,
				# 	'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				# 	'token': generate_token.make_token(user),
				# 	'protocol': 'https' if request.is_secure() else 'http'
				# })
				#
				# messages.success(request, f"{message}")

				# email = EmailMessage(
				# 	email_subject,
				# 	message,
				# 	settings.EMAIL_HOST_USER,
				# 	[email],
				# )
				# if email.send():
				# 	messages.success(request, "Go check you email")
				# else:
				# 	messages.error(request, "Some error occured")
				#
				# messages.success(request, f"Click to activation link sent on {email}")

				return redirect('sign-up')
		else:
			messages.warning(request, "Password doesn't match")
			return redirect('sign-up')
	else:
		context = {"load_form": "sign-up", "title": "Sign Up"}
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
