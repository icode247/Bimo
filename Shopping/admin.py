from django.contrib import admin
from .models import Order,product,OrderedItem

admin.site.register(Order)
admin.site.register(product)
admin.site.register(OrderedItem)


