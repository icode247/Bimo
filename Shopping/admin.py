from django.contrib import admin
from .models import Order, product, OrderedItem, BillingAddress, Payment, Contact

admin.site.register(Order)
admin.site.register(product)
admin.site.register(OrderedItem)
admin.site.register(BillingAddress)
admin.site.register(Payment)
admin.site.register(Contact)
