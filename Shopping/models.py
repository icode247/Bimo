from django.db import models
from django.conf import settings
import random
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404, reverse, render, redirect
from django_countries.fields import CountryField
from uuid import uuid4

auto_generate_id = random.randint(12845, 67590)
auto_id = 'shop' + str(auto_generate_id)

PRODUCT_ID = random.randint(123456, 987654)

PRODUCT_TYPE = [
    ('FS', "Fashion"),
    ('PT', "Phone & Tablets"),
    ('EL', "Electronics"),
    ('HO', "Home & Office"),
    ('CP', "Computing"),
]

PRODUCT_SIZE = [
    ('SM', "Small"),
    ('MD', "Medium"),
    ('LG', "Large"),
    ('VG', "Very Large"),
]

PRODUCT_COLORS =[
    ('RED', "Red"),
    ('BLU', "Blue"),
    ('BLK', "Black"),
    ('ORG', "Orange"),
    ('PIN', "Pink"),
    ('PUR', "Purple"),
    ('BRW', "Brown"),
    ('CRM', ""),
]

def save_sample_with_uiid(instance, filname):
    return '{}{}'.format(instance.slug,uuid4())

class product(models.Model):
    slug = models.SlugField(default=PRODUCT_ID)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField(null=True, blank=True)
    P_type = models.CharField(choices=PRODUCT_TYPE, max_length=2)
    sample = models.ImageField(upload_to=save_sample_with_uiid)
    available_item = models.IntegerField()
    Date = models.DateTimeField(auto_now=True)
    Time = models.TimeField(auto_now=True)

    class Meta:
        ordering = ['-Date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Product_Single', args=[str(self.slug)])

    def get_cart_url(self):
        return reverse('add_to_cart', kwargs={'slug': self.slug})

    def get_remove_cart(self):
        return reverse('remove_cart', kwargs={'slug': self.slug})


class OrderedItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quantity} of {self.item}'

    def item_total(self):
        return self.quantity * self.item.price

    def get_discount_price(self):
        if self.item.discount:
            return self.quantity * self.item.discount

    def get_saved_amount(self):
        return self.item_total() - self.get_discount_price()

    def get_final_price(self):
        return self.item_total()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderedItem)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    billing_address = models.ForeignKey(
        'BillingAddress', on_delete=models.SET_NULL, null=True, blank=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_sub_total(self):
        return sum([order_item.item.price * order_item.quantity for order_item in self.items.all()])
    
    def get_total_price(self):
         return sum([order_item.item.price * order_item.quantity + 1500 for order_item in self.items.all()])
    


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=10)
    street_address = models.CharField(max_length=100)
    apartment = models.CharField(max_length=100)
    Town = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Email = models.EmailField()
    payment_type = models.CharField(max_length=2)

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    strip_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.user.username


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('Contact')
