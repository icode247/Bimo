from django.conf.urls import url
from django.urls import path, reverse,reverse_lazy
from . views import (
    Index,
    Fashion,
    Product_Single,
    Add_To_Cart,
    Electronics,
    Home_Office,
    Computing,
    Phones,
    About,
    Contact,
    Cart,
    Checkout,


)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('Checkout/',Checkout.as_view(), name='Checkout'),
    path('Cart/',Cart.as_view(), name="Cart"),
    path('Contact/',Contact.as_view(), name='Contact'),
    path('About/', About.as_view(), name='About'),
    path('Phones/', Phones, name='Phone'),
    path('Home_Office/',Home_Office, name='Home'),
    path('Computing/', Computing, name='Computing'),
    path('Electronics/', Electronics, name='Electronics'),
    path('add_to_cart/<slug>', Add_To_Cart, name='add_to_cart'),
    path('Fashion/<slug>', Product_Single.as_view(), name='Product_Single'),
    path('Fashion/', Fashion.as_view(), name='Fashion'),
    path('', Index.as_view(), name = 'Index'),
]

urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
