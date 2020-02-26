from django.views.generic import (
TemplateView,
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView
)
from . models import Product,Ordered_Item,User_Order
from django.shortcuts import redirect,get_list_or_404,render,HttpResponse

class Index(TemplateView):

    template_name = 'index.html'

class Fashion(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'

class Product_Single(DeleteView):
    model = Product
    template_name = 'product-single.html'

def Electronics(request):
  product = Product.objects.order_by('-title')
  return render(request,'electronics.html', {'Electronics':product})

def Computing(request):
   product = Product.objects.order_by('-title')
   return render(request,'electronics.html', {'Computing':product})

def Home_Office(request):
   product = Product.objects.order_by('-title')
   return render(request,'electronics.html', {'Phones':product})

def Phones(request):
     product = Product.objects.order_by('-title')
     return render(request,'electronics.html', {'Home_Ofice':product})

class About(TemplateView):
    template_name = 'about.html'

class Contact(TemplateView):
    template_name = 'contact.html'

class Cart(ListView):
   model = User_Order
   template_name = 'cart.html'

class Checkout(CreateView):
    model = User_Order
    template_name = 'checkout.html'
    fields = '__all__'

def Add_To_Cart(request, slug):
    items = get_list_or_404(Product, slug=slug)
    Ordered_Item.objects.create(quantity=+1)
    return HttpResponse('hello')


