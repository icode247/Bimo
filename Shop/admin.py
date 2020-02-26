from django.contrib import admin
from .models import Shop,Product,Ordered_Item,User_Order

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Ordered_Item)
admin.site.register(User_Order)
