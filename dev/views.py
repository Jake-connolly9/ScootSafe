from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Device_Group, Device
from .forms import CreateDevice, Login, Register_Account

# Create your views here.

def FMD(request):
    ls = Device_Group.objects.get(id=1)
    return render(request,'MapView.html', {"ls":ls}) 

def choice(request):
    if request.method == "POST":
        form = CreateDevice(request.POST)

        if form.is_valid():
            n = form.cleaned_data["device_name"]
            la = form.cleaned_data["gps_latitude"]
            lo = form.cleaned_data["gps_longtitude"]
            a = Device_Group(id=1)
            a.device_set.create(device_name = n, gps_latitude = la, gps_longtitude = lo)
            a.save()

    else:
        form = CreateDevice()
    return render(request,'ViewChoice.html', {"form":form})

def login(request):
    if request.method == "POST":
        form = Login(request.POST)
        
        if form.is_valid():
            user = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
        return HttpResponseRedirect("choice")
    else:
        form = Login()
    return render(request, 'LoginPage.html', {"form":form})

def BlackBox(request):
    return render(request, 'BlackboxView.html')

def SignUp(request):
        if request.method == "POST":
            form = Register_Account(request.POST)
        
            if form.is_valid():
                user = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
            return HttpResponseRedirect("/dev/choice")
        else:
            form = Register_Account()
        return render(request, 'SignUp.html', {"form":form})