from .models import TrackOrders  # Import necessary models if needed

def cart_count(request):
    if request.user.is_authenticated:
        cart_items_count = TrackOrders.objects.filter(user=request.user).count()
    else:
        cart_items_count = 0

    return {'cart_items_count': cart_items_count}
