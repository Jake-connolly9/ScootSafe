from django.shortcuts import render
from django.http import HttpResponse
from .models import Device_Group, Device
from .forms import CreateDevice

# Create your views here.

def FMD(request):
    ls = Device_Group.objects.get(id=1)
    return render(request,'MapView.html', {"ls":ls}) 

def choice(request):
    form = CreateDevice()
    return render(request,'ViewChoice.html', {"form":form})

def login(request):
    return render(request, 'LoginPage.html')

def BlackBox(request):
    return render(request, 'BlackboxView.html')