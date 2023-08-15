from .models import Product, Category
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q


def all_products(request):
    ''' A view to diplay all products, filtering & searching '''
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:

        # CATEGORY
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # SEARCH ENGINE
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'No queries found!')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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
