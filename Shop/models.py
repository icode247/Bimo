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
class Shop(models.Model):

    #manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shop_id = models.SlugField(default=auto_id)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True, max_length=200)
    passport = models.ImageField(default='noimage.png')
    pvc = models.ImageField(default='noimage.png')

    def __str__(self):
        return self.shop_id + '({})'.format(self.shop_id)

class Product(models.Model):

    #shop = models.ManyToManyField(Shop)
    slug = models.SlugField(default=PRODUCT_ID)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField()
    type = models.CharField(max_length=2, choices = PRODUCT_TYPE)
    size = models.CharField(max_length=2 , choices=PRODUCT_SIZE)
    sample = models.ImageField(default='noimage.png',blank=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title + '({})'.format(self.slug)

    def get_absolute_url(self):
         return reverse('Fashion', args={'slug':self.slug
         })

    def get_add_to_cart_url(self):
        return reverse('add_to_cart', kwargs={'slug':self.slug})


class Ordered_Item(models.Model):

     item = models.ManyToManyField(Product)
     quantity = models.IntegerField(default=1)

     def __str__(self):
         return str(self.quantity)


class User_Order(models.Model):

     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     items = models.ManyToManyField(Ordered_Item)
     Date_Orderd = models.DateTimeField(auto_now_add=True)
     Odered = models.BooleanField(default=False)

     def __str__(self):
         return self.user.username






