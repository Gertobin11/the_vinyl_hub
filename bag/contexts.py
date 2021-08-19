from django.conf import settings

from decimal import Decimal


def bag_contents(request):
    bag_items = []
    sale_items = []
    total = 0
    product_count = 0

    # function to check if more then 1 hip hop item were bought
    for bag_item in bag_items:
        if bag_item.product.category == 'hip_hop':
            sale_items.append(bag_item)
            if sale_items > 1:
                for sale_item in sale_items:
                    sale_item.product.price = (sale_item.product.price
                                               * Decimal(20 / 100))
                    bag_items.append(sale_item)
            else:
                for sale_item in sale_items:
                    bag_items.append(sale_item)

    ''' Code to see if free delivery criteria has been met,
     learned during Code Institute course '''
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
