from django import forms

from myapp.models import *


class Doctor_Form (forms.ModelForm):
    f_name = forms.CharField (max_length=100, widget=forms.TextInput (attrs={'class': "input--style-4"}))
    l_name = forms.CharField (max_length=100, widget=forms.TextInput (attrs={'class': "input--style-4"}))
    email = forms.EmailField (max_length=100, required=True,
                              widget=forms.EmailInput (attrs={'class': "input--style-4"}))
    username = forms.CharField (max_length=50, required=True,
                                widget=forms.TextInput (attrs={'class': "input--style-4"}))
    password = forms.CharField (max_length=20, required=True,
                                widget=forms.PasswordInput (attrs={'class': "input--style-4"}))
    confirm_password = forms.CharField (max_length=20, required=True,
                                        widget=forms.PasswordInput (attrs={'class': "input--style-4"}))

    class Meta:
        model = Doctor
        fields = ['f_name', 'l_name', 'email', 'username', 'password', 'confirm_password']


class Patient_Form (forms.ModelForm):
    f_name = forms.CharField (max_length=50, widget=forms.TextInput (attrs={'class': "input--style-4"}))
    l_name = forms.CharField (max_length=50, widget=forms.TextInput (attrs={'class': "input--style-4"}))
    email = forms.EmailField (max_length=50, widget=forms.TextInput (attrs={'class': "input--style-4"}))
    address = forms.CharField (max_length=500, widget=forms.TextInput (attrs={'class': "input--style-4"}))
    age = forms.IntegerField (widget=forms.TextInput (attrs={'class': "input--style-4"}))
    contact_no = forms.IntegerField (widget=forms.TextInput (attrs={'class': "input--style-4"}))

    class Meta:
        model = Patient
        fields = ['f_name', 'l_name', 'email', 'address', 'age', 'contact_no']
