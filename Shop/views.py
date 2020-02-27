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
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required


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
    items = get_list_or_404(Ordered_Item)
    User_Order.objects.create(items=items)
    return HttpResponse('hello')

def Customer_Signup(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('Index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html',{"form":form})

def Customer_Login(request):

   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():

          user = form.get_user()
          login(request, user)
          return redirect('Index')

      else:
          redirect('home')
   else:
       form = AuthenticationForm()

   return  render(request,'registration/login.html', {"form":form})

def Customer_Logout(request):
    if request.method == "POST":
       logout(request)
    return redirect('home')

class Add(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'add.html'

