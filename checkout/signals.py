from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


# receivers copied from Boutique Ado
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    '''
    update order_total on lineitem create update
    '''
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    '''
    update order_total on lineitem delete
    '''
    instance.order.update_total()
