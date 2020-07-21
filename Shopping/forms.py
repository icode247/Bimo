from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_OPTIONS = {
    ('D', 'Direct Bank Transfer'),
    ('S', 'Strip'),
    ('P', 'Paypal'),
}
PAYMENT_TYPE = {
    ('PO','Pay online'),
    ('PD','Pay on delivery'),
}

class CheckoutForm(forms.Form):
    country = CountryField(blank_label='(Select Country)').formfield(widget=CountrySelectWidget(
        attrs={"class": "form-control"}
    ))
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'House number and street name',
        'class': 'form-control'
    }))
    apartment = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Appartment, suite, unit etc: (optional)',
        'class': 'form-control',
    }))
    Town = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'City or nearest town',
        'class': 'form-control'
    }))
    zip = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    Phone = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    payment_Type = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_TYPE, required=True)
    payment_method = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_OPTIONS)

class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)
