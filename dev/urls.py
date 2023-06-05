from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admins/', admin.site.urls),
    path('choice/FMD/', views.FMD),
    path('', views.login),
    path('choice/blackbox/', views.BlackBox),
    path('choice/', views.choice),
    path('SignUp/', views.SignUp)
]

urlpatterns += staticfiles_urlpatterns()