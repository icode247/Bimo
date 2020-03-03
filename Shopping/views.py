from django.views.generic import (
TemplateView,
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView,
View,
)
from . models import product,OrderedItem,Order,BillingAddress,Payment,Contact
from django.shortcuts import redirect,get_object_or_404,render,HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import CheckoutForm
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import stripe
sripe_token_api = settings.STRIPE_SECRET_KEY
from django.contrib.messages.views import SuccessMessageMixin




class Index(LoginRequiredMixin,ListView):
    context_object_name = 'products'
    queryset = product.objects.order_by('-Date')
    template_name = 'index.html'
    paginate_by = 8

class Fashion(LoginRequiredMixin,ListView):
    context_object_name = 'products'
    queryset = product.objects.filter(P_type='FS')
    template_name = 'shop.html'
    paginate_by = 6


class Product_Single(DeleteView):
    model = product
    template_name = 'product-single.html'

@login_required()
def Electronics(request):
  products = product.objects.filter(P_type='EL')
  context = {'Electronic':products}
  return render(request,'electronics.html',context)

@login_required()
def Computing(request):
   products = product.objects.filter(P_type='CP')
   context = {'Computing':products}
   return render(request,'computing.html', context)

@login_required()
def Home_Office(request):
   products = product.objects.filter(P_type="HO")
   return render(request,'home_office.html', {'Home':products})

@login_required()
def Phones(request):
     products = product.objects.filter(P_type="PT")
     return render(request,'phone_tablet.html', {'Home_Office':products})


class About(LoginRequiredMixin,TemplateView):
    template_name = 'about.html'


class Contact(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model = Contact
    template_name = 'contact.html'
    fields = ['name','email','subject','message']
   # success_message = 'Message successfully sent, We will get back to you'


class Cart(LoginRequiredMixin,ListView):
   model = OrderedItem
   template_name = 'cart.html'


class Cart(LoginRequiredMixin,View):
   def get(self, *args, **kwargs):
       try:
           order = Order.objects.get(user=self.request.user, status=False)
           context = {
               'object':order
           }
           return render(self.request, 'cart.html', context)
       except ObjectDoesNotExist:
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
            redirect('Cart')
        else:
            redirect('Cart')
    return redirect("Cart")


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

class Checkout(View):
    def get(self,*args, **kwargs):
        form = CheckoutForm()
        order = Order()
        context = {
            'form':form,
            'order':order,
        }
        return render(self.request,'checkout.html', context)

    def post(self,*args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
           order = Order.objects.get(user=self.request.user, status=False)
           if form.is_valid():
             country = form.cleaned_data.get('counntry')
             street_address = form.cleaned_data.get('street_address')
             apartment = form.cleaned_data.get('apartment')
             Town = form.cleaned_data.get('Town')
             zip = form.cleaned_data.get('zip')
             Phone = form.cleaned_data.get('Phone')
             Email = form.cleaned_data.get('Email')
             same_billing_address = form.cleaned_data.get('same_billing_address')
             save_info = form.cleaned_data.get('save_info ')
             payment_method = form.cleaned_data.get('payment_method')

             billing_address = BillingAddress(
                 user = self.request.user,
                 country=country,
                 street_address = street_address,
                 apartment = apartment,
                 Town = Town,
                 zip = zip,
                 Phone = Phone,
                 Email = Email
             )
             billing_address.save()
             order.billing_address = billing_address
             order.save()
             messages.success(self.request,"Check out was successful")
             return redirect('Checkout')
          # messages.warning(self.request,"Checkout Failed")
           return redirect('Payment')
        except ObjectDoesNotExist:
              return redirect('Payment')

class Payment(View):
    def get(self, *args, **kwargs):
        return render(self.request,'payment.html')

    def post(self, *args, **kwargs):
        order = Order.objects.get(user = self.request.user, status = False)
        token = self.request.POST.get('stripeToken')
        amount = order.get_total() * 100

        try:
            charge = stripe.Charge.create(
            amount = amount,
            currency = 'usd',
            source = token,
            )
            payment = Payment()
            payment.strip_charge_id = charge['id']
            payment.user = self.request.user
            payment.amount = amount
            payment.save()

            order.status = True
            order.payment = payment

            messages.success(self.request, "You order was succesful")
            return redirect('Cart')
        except stripe.error.CardError as e:
          # Since it's a decline, stripe.error.CardError will be caught

          print('Status is: %s' % e.http_status)
          print('Type is: %s' % e.error.type)
          print('Code is: %s' % e.error.code)
          # param is '' in this case
          print('Param is: %s' % e.error.param)
          print('Message is: %s' % e.error.message)
          return redirect('Cart')
        except stripe.error.RateLimitError as e:
          # Too many requests made to the API too quickly
          messages.error(self.request,'Rate limit error')
          return redirect('Cart')
        except stripe.error.InvalidRequestError as e:
          # Invalid parameters were supplied to Stripe's API
          messages.error(self.request,'Invalid request eror')
          return redirect('Cart')
        except stripe.error.AuthenticationError as e:
          # Authentication with Stripe's API failed
          # (maybe you changed API keys recently)
          messages.error(self.request,'Authentification error')
          return redirect('Cart')
        except stripe.error.APIConnectionError as e:
          # Network communication with Stripe failed
          messages.error(self.request,'Network error ')
          return redirect('Cart')
        except stripe.error.StripeError as e:
          # Display a very generic error to the user, and maybe send
          # yourself an email
          messages.error(self.request,'Stripe Error')
          return redirect('Cart')
        except Exception as e:
          # Something else happened, completely unrelated to Stripe
          messages.error(self.request,'we have been notifeid, we will get back to you.')
          return redirect('Cart')


