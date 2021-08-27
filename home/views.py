from django.shortcuts import render


def index(request):
    ''' A view to return the index page '''
    return render(request, 'home/index.html')


def requests(request):
    ''' A view to return requests '''
    return render(request, 'home/requests.html')
