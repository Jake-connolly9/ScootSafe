from django import forms

class CreateDevice(forms.Form):
    device_name = forms.CharField(max_length=15,label="Name")
    gps_latitude = forms.DecimalField(decimal_places=2)
    gps_longtitude = forms.DecimalField(decimal_places=2)

class Login(forms.Form):
    username = forms.CharField(max_length=15,label="User")
    password = forms.CharField(max_length=15,label="Pass")

class Register_Account(forms.Form):
    username = forms.CharField(max_length=15,label="User")
    password = forms.CharField(max_length=15,label="Pass")
    confirm_pass = forms.CharField(max_length=15,label="Confirm Pass")
    email = forms.CharField(max_length=25,label="Email")
