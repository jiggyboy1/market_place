from typing import Any
from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm


class UserInfo(forms.ModelForm):
    phone = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),required=False)
    address1 = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address1'}),required=False)
    address2 = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address2'}),required=False)
    city =  forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'city'}),required=False)
    country = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'country'}),required=False)
    
    
    class Meta:
        model = Profile
        fields = ['phone','address1','address2','city','country','image']

class Register_form(UserCreationForm):
    email = forms.EmailField(max_length=40,widget=forms.EmailInput(attrs={'class':'form-control'}),required=False)
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}),required=False)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(Register_form,self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'


class Updateuserform(UserChangeForm):
    password = None
    email = forms.EmailField(max_length=40,widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name',]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(Updateuserform,self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class']='form-control'

class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1','new_password2']


    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(ChangePasswordForm,self).__init__(*args, **kwargs)
        
        self.fields['new_password1'].widget.attrs['class']='form-control'
        self.fields['new_password2'].widget.attrs['class']='form-control'


