from django import forms
from accounts.models import myUser
from buyer.models import Order

class ProductOrderForm(forms.ModelForm):
    pass

class ProductSearchForm(forms.Form):
    search= forms.CharField(max_length = 200)
