from django.shortcuts import render, HttpResponse, redirect
from .models import Product, TrackOrders
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


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


def view_cart(request):
	# Fetch TrackOrders for the current user
	items = TrackOrders.objects.filter(user=request.user)

	# Fetch all Product details for the product_ids in items
	product_ids = items.values_list('product_id', flat=True)
	product_details = Product.objects.filter(id__in=product_ids)

	# Print product details for debugging
	total = 0
	for product in product_details:
		total += product.price
		print(f"\n\n{product.price}\n\n")

	print(total)

	# Prepare the context for the template
	context = {'items': product_details, 'total': total}
	return render(request, 'cart.html', context=context)


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    track_order, created = TrackOrders.objects.get_or_create(user=request.user, product_id=product_id)
    # Logic to handle quantities can be added here, for now we're just adding the item
    return redirect('cart')

@login_required
def remove_from_cart(request, product_id):
    TrackOrders.objects.filter(user=request.user, product_id=product_id).delete()
    return redirect('cart')


def checkout(request):
	return render(request, 'checkout.html')


def blog(request):
	pass


def orders(request):
	pass


def my_profile(request):
	pass


def cart(request):
	pass
