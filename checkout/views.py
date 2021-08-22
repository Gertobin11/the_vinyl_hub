from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    ''' A function to bring the user to the checkout page,
     where he can see his order summary,
    and complete his order by completing the form and
    entering his payment details '''
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    template = 'checkout/checkout.html'
    order_form = OrderForm
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
