from django.shortcuts import render


from .models import Product
from .forms import ProductForm


def all_products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)
