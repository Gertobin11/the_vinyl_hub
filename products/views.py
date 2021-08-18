from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product


def all_products(request):
    ''' A view to show all the products including  searches and sorting'''

    products = Product.objects.all()
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search terms!")
                return redirect(reverse('products'))

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    ''' A view to show the user their selected product'''

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }

    return render(request, 'products/product_details.html', context)
