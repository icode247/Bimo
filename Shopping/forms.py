from django import forms

PRODUCT_SIZES =  [
    ('SM',"Small"),
    ('MD',"Medium"),
    ('LG',"Large"),
    ('VG',"Very Large"),
]
class Add_to_Cart(forms.Form):
    size =  forms.TypedChoiceField(choices=PRODUCT_SIZES)
