from django.shortcuts import render, HttpResponse
from .models import Product


# Create your views here.
def home(request):
	all_products = Product.objects.all()
	context = {'products': all_products}
	return render(request, 'index.html', context=context)


def add_item(request):
	x = request.GET['id']
	y = request.user.username

	return HttpResponse(y)


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
