from django import forms

class CreateDevice(forms.Form):
    device_name = forms.CharField(max_length=15,label="Name")
    gps_latitude = forms.DecimalField()
    gps_longtitude = forms.DecimalField()
