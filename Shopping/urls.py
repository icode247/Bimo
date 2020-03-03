from django.conf.urls import url, include
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
    Customer_Login,
    Customer_Logout,
    Customer_Signup,
    Add,
    #Order_summary,
    remove_from_Cart,
    Payment


)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('Payment/',Payment.as_view(), name="Payment"),
   #path('Cart/', Order_summary, name="Cart"),
    path('Checkout/',Checkout.as_view(), name="Checkout"),
    path('Add/',Add.as_view(), name='Add'),
    path('Cart/',Cart.as_view(), name='Cart'),
    path('Contact/',Contact.as_view(), name='Contact'),
    path('About/', About.as_view(), name='About'),
    path('Phones/', Phones, name='Phone'),
    path('Home_Office/',Home_Office, name='Home'),
    path('Computing/', Computing, name='Computing'),
    path('Electronics/', Electronics, name='Electronics'),
    path('add_to_cart/<slug>', Add_To_Cart, name='add_to_cart'),
    path('remove_from_cart/<slug>',remove_from_Cart, name='remove_cart'),
    path('Fashion/<slug>', Product_Single.as_view(), name='Product_Single'),
    path('Fashion/', Fashion.as_view(), name='Fashion'),
    path('Signup/', Customer_Signup, name='Signup'),
    path('', Customer_Login , name='home'),
    path('Logout/',Customer_Logout, name='Logout'),
    path('Home/', Index.as_view(), name = 'Index'),
]



