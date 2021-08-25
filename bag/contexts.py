from django.conf import settings
from django.shortcuts import get_object_or_404

from products.views import Product
from decimal import Decimal


def bag_contents(request):
    bag_items = []
    discount = 0
    subtotal = 0
    subtotals = []
    new_total = 0
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        bag_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })

    ''' code to check if more then 1 hip hop item were bought and are registered
        it first check if the item has the chosen category which is on sale.
         If the condition is  met it applies a 15% discount '''
    if request.user.is_authenticated:
        for bag_item in bag_items:
            if bag_item['product'].category.name == 'hip_hop':
                bi_price = bag_item['product'].price
                bi_price = bi_price - (bi_price * 15 / 100)
                bi_price = Decimal(bi_price.quantize(Decimal('.01')))
                bag_item['product'].price = bi_price
    if bag_items:
        for bag_item in bag_items:
            subtotal = Decimal(bag_item['quantity']) * (bag_item[
                                                        'product'].price)
            subtotals.append(subtotal)

    new_total = sum(subtotals)

    discount = total - new_total

    ''' Code to see if free delivery criteria has been met,
     learned during Code Institute course '''
    if new_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = new_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE
                                       / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + new_total

    context = {
        'bag_items': bag_items,
        'bag': bag,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'discount': discount,
        'new_total': new_total
    }

    return context
