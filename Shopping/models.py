from django.db import models
from django.conf import settings
import random
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404,reverse,render,redirect

auto_generate_id = random.randint(12345,67890)
auto_id = 'shop' + str(auto_generate_id)

PRODUCT_ID = random.randint(123456,987654)

PRODUCT_TYPE = [
    ('FS',"Fashion"),
    ('PT',"Phone & Tablets"),
    ('EL',"Electronics"),
    ('HO',"Home & Office"),
    ('CP',"Computing"),
]

PRODUCT_SIZE =  [
    ('SM',"Small"),
    ('MD',"Medium"),
    ('LG',"Large"),
    ('VG',"Very Large"),
]

class product(models.Model):
    slug = models.SlugField(default=PRODUCT_ID)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField(null=True, blank=True)
    P_type = models.CharField(choices=PRODUCT_TYPE, max_length=2)
    size = models.CharField(choices=PRODUCT_SIZE, max_length=2)
    sample = models.ImageField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):

        return reverse('Product_Single', args=[str(self.slug)])


    def get_cart_url(self):
        return reverse('add_to_cart', kwargs={'slug':self.slug})

    def get_remove_cart(self):
        return reverse('remove_cart', kwargs={'slug':self.slug})

class OrderedItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    #seize = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quantity} of {self.item}'



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderedItem)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


