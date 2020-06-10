from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg',registration),
    path('login',login),
    path("signIn",inserttotable,name="signIn"),

]