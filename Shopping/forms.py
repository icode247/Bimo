from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_OPTIONS = {
    ('D','Direct Bank Trnasfer'),
    ('S','Strip'),
    ('P','Paypal'),
}
class CheckoutForm(forms.Form):

    country = CountryField(blank_label='(Select Country)').formfield(widget=CountrySelectWidget(
           attrs={"class": "form-control"}
        ))
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'House number and street name',
        'class':'form-control'
    }))
    apartment = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'placeholder':'Appartment, suite, unit etc: (optional)',
         'class':'form-control',
    }))
    Town = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'City or nearest town',
         'class':'form-control'
    }))
    zip = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    Phone = forms.IntegerField()
    Email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control'
    }))
    same_billing_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_method = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_OPTIONS)
