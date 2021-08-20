from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    ''' A view to allow the user to see their shopping bag '''
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    ''' Function to add items to the bag '''

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust an item in the shopping bag shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove an item in the shopping bag shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'error removing item: {e}')
        return HttpResponse(status=500)
