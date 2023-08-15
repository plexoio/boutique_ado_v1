from .models import Product, Category
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q


def all_products(request):
    ''' A view to diplay all products, filtering & searching '''
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        # SORTING
        if 'sort' in request.GET:
            sort = request.GET['sort']
            if 'key' in sort:
                sort = 'lower_key'
                products = products.annotate(lower_key=Lower('key'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if 'desc' in direction:
                    sort = f'-{sort}'
            products = products.order_by(sort)

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

    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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
