from django.shortcuts import render

from products.models import ProductsCategory, Product

# Create your views here.

def index(request):
    context = {
        'title': 'Store',

    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store',
        'categories' : ProductsCategory.objects.all(),
        'products' : Product.objects.all(),
    }
    return render(request, 'products/products.html', context)