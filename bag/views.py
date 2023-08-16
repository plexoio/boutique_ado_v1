from django.shortcuts import render


def view_bag(request):
    ''' Return view of bag contents '''
    return render(request, 'bag/bag.html')
