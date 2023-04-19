from django.urls import path
from . import views

urlpatterns = [
    path('choice/FMD/', views.FMD),
    path('', views.login),
    path('choice/blackbox/', views.BlackBox),
    path('choice/', views.choice),
]