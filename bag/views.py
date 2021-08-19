from django.shortcuts import render


def view_bag(request):
    ''' A view to allow the user to see their shopping bag '''
    return render(request, 'bag/bag.html')
