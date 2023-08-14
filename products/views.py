from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    ''' A view to diplay all products, filtering & searching '''
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)


def product_datail(request, product_id):
    ''' Get the passed product view to diplay it using context'''

    # 'pk' stands for primary key

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)
