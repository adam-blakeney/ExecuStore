from django.shortcuts import render


from .models import Product
from .forms import ProductForm


def all_products(request):
    products = Product.objects.all()

    data = {
        'products': products
    }

    return render(request, 'base.html', data)
