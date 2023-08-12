from django.shortcuts import render


def index(request):
    ''' Return view for homepage '''
    return render(request, 'home/index.html')
