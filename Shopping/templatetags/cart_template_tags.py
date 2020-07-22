from django import template
from Shopping.models import Order, OrderedItem

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, status=False)
        if qs.exists():
            return qs[0].items.count()
    return 0


@register.filter
def Cart_item_quantity(user):
    if user.is_authenticated:
        qs = OrderedItem.objects.filter(user=user, status=False)
        if qs.exists():
            return qs[0].quantity
        return 0


@register.filter
def item_sub_total(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, status=False)
        if qs.exists:
            return qs[0].get_sub_total()
        return 0


@register.filter
def get_total_order(user):
    if user.is_authenticated:
        qs = order = Order.objects.filter(user=user, status=False)
        if qs.exists:
            return qs[0].get_total_price()
        return 0
