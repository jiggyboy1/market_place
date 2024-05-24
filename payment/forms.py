from django import forms
from .models import ShippingAddress




class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),required=True)
    shipping_email = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}),required=True)
    shipping_address1 = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address1'}),required=True)
    shipping_address2 = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address2'}),required=False)
    shipping_city = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'city'}),required=True)
    shipping_country = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'country'}),required=True)
    shipping_state = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'State'}),required=False)
    shipping_zipcode = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Zipode'}),required=False)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name','shipping_email','shipping_address1','shipping_address2','shipping_city','shipping_country','shipping_state','shipping_zipcode']
        exlude = ['user',]