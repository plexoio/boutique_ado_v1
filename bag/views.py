from django.shortcuts import render, redirect


def view_bag(request):
    ''' Return view of bag contents '''
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    ''' For users to add desired product into the bag.
    This will fill the session with data to be used on the 'bag_contents'
    definition at contexts.py'''
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST.get('product_size')

    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
