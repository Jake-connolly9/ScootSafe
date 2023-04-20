from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('choice/FMD/', views.FMD),
    path('', views.login),
    path('choice/blackbox/', views.BlackBox),
    path('choice/', views.choice),
]