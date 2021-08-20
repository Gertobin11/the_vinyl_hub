from django import template

register = template.Library()


# Function from Code Institute taken from the Django documentation
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
