from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm


class Register_form(UserCreationForm):
    email = forms.EmailField(max_length=40,widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))

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
