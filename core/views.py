from django.shortcuts import render, HttpResponse, redirect
from .models import Product, TrackOrders
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def home(request):
	all_products = Product.objects.all()
	context = {'products': all_products}
	return render(request, 'index.html', context=context)


@login_required(login_url='sign-in')
def add_item(request):
	# Get product ID from the request
	product_id = request.GET.get('id')

	# Get the current user
	user = request.user

	# Ensure product_id is provided and valid
	if product_id:
		try:
			product_id = int(product_id)
		except ValueError:
			# Handle invalid product ID
			return HttpResponse('Invalid product ID')

		# Create and save the new TrackOrders object
		order = TrackOrders(product_id=product_id, user=user)
		order.save()

		# Redirect to a success page or render a success template
		return redirect('home')  # Change to your success URL or view name

	# Handle the case where product_id is not provided
	return HttpResponse('Product ID is required')

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
