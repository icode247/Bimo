from django.views.generic import (
TemplateView,
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView,
View,
)
from . models import product,OrderedItem,Order
from django.shortcuts import redirect,get_object_or_404,render,HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import Add_to_Cart
from django.core.exceptions import ObjectDoesNotExist



class Index(LoginRequiredMixin,TemplateView):

    template_name = 'index.html'

class Fashion(LoginRequiredMixin,ListView):
    context_object_name = 'products'
    queryset = product.objects.all()
    template_name = 'shop.html'
    paginate_by = 6


class Product_Single(DeleteView):
    model = product
    template_name = 'product-single.html'

@login_required()
def Electronics(request):
  obj = get_list_or_404(product)
  context = {'item':obj
             }
  return render(request,'electronics.html',context)

@login_required()
def Computing(request):
   products = product.objects.all()
   context = {'Computing':products}
   return render(request,'computing.html', context)

@login_required()
def Home_Office(request):
   products = product.objects.order_by('-title')
   return render(request,'electronics.html', {'Phones':products})

@login_required()
def Phones(request):
     products = product.objects.order_by('-title')
     return render(request,'electronics.html', {'Home_Ofice':product})


class About(LoginRequiredMixin,TemplateView):
    template_name = 'about.html'


class Contact(LoginRequiredMixin,TemplateView):
    template_name = 'contact.html'


class Cart(LoginRequiredMixin,ListView):
   model = OrderedItem
   template_name = 'cart.html'


class Checkout(LoginRequiredMixin,View):
   def get(self, *args, **kwargs):
       try:
           order = Order.objects.filter(user=self.request.user, status=False)
           context = {
               'object':order
           }
           return render(self.request, 'cart.html', context)
       except ObjectDoesNotExist:
            messages.error(self.request, "No item in your cart")
            return render(self.request, 'cart.html', context)


@login_required()
def Add_To_Cart(request, slug):
    item = get_object_or_404(product, slug=slug)
    cart, created = OrderedItem.objects.get_or_create(item=item, user=request.user, status=False)
    qs = Order.objects.filter(user=request.user, status=False)
    if qs.exists():
        order = qs[0]
        if order.items.filter(item__slug = item.slug).exists():
            cart.quantity +=1
            cart.save()
            messages.info(request, 'Cart was modified')
            redirect('Product_Single', slug=slug)
        else:
            order.items.add(cart)
            messages.info(request, 'Item was added to cart')
            redirect('Product_Single', slug=slug)
    else:
        order = Order.objects.create(user = request.user)
        order.items.add(cart)
        messages.info(request, 'Item was added to cart')
        redirect('Product_Single', slug=slug)

    return redirect("Product_Single", slug=slug)

@login_required()
def remove_from_Cart(request, slug):
    item = get_object_or_404(product, slug=slug)
    qs = Order.objects.filter(user=request.user, status=False)
    if qs.exists():
        order = qs[0]
        if order.items.filter(item__slug = item.slug).exists():
            cart = OrderedItem.objects.filter(
                item=item,
                user=request.user,
                status=False)[0]

            messages.error(request, 'Item was removed from cart')
            order.items.remove(cart)
            redirect('Product_Single', slug=slug)
        else:
            redirect('Product_Single', slug=slug)
    return redirect("Product_Single", slug=slug)


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

class Add(LoginRequiredMixin,CreateView):
    model = product
    fields = '__all__'
    template_name = 'add.html'

def Order_summary(request, user):
        order = OrderedItemr.objects.get(user=request.user, Odered= False)
        context ={
            "object":order
        }
        return render(request, 'cart.html', context)


