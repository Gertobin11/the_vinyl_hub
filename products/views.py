from django.shortcuts import render, get_object_or_404

from .models import Product


def all_products(request):
    ''' A view to show all the products including  searches and sorting'''

    products = Product.objects.all()
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
