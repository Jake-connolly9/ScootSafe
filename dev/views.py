from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def FMD(request):
    return render(request,'MapView.html')

def choice(request):
    return render(request,'ViewChoice.html')

def login(request):
    return render(request, 'LoginPage.html')

def BlackBox(request):
    return render(request, 'BlackboxView.html')