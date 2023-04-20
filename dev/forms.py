from django import forms

class CreateDevice(forms.Form):
    device_name = forms.CharField(max_length=15,label="Name",required=True)
    gps_latitude = forms.DecimalField(decimal_places=2,required=True)
    gps_longtitude = forms.DecimalField(decimal_places=2,required=True)

class Login(forms.Form):
    username = forms.CharField(max_length=15,label="User",required=True)
    password = forms.CharField(max_length=15,label="Pass",required=True)

class Register_Account(forms.Form):
    username = forms.CharField(max_length=15,label="User",required=True)
    password = forms.CharField(max_length=15,label="Pass",required=True)
    confirm_pass = forms.CharField(max_length=15,label="Confirm Pass",required=True)
    email = forms.CharField(max_length=25,label="Email",required=True)
