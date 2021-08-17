from django.shortcuts import render

from .models import Product

products = Product.objects.all()

context = {
    'products': products
}


def all_products(request):
    ''' A view to show all the products including  searches and sorting'''
    return render(request, 'products/products.html', context)
