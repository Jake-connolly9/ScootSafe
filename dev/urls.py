from django.urls import path
from . import views

urlpatterns = [
    path('login/choice/FMD/', views.FMD),
    path('login/', views.login),
    path('login/choice/blackbox/', views.BlackBox),
    path('login/choice/', views.choice),
]