from django import forms
from .models import *


class AddProductForm(forms.ModelForm):
    name=forms.CharField(max_length=254)
    category=forms.CharField()
    description=forms.CharField(widget=forms.Textarea)
    product_image=forms.FileField()
    stock=forms.IntegerField()
    
    class Meta:
        model=Product
        fields = ('name','category','description','product_image','stock')

