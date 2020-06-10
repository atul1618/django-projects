from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def registration(request):
#     return HttpResponse("<h1>inside student register</h1")
#
# def login(request):
#     return HttpResponse("<h1>loginpage</h1>")

def registration(request):
    return render(request,"students/reg.html")

def login(request):
    return render(request,"students/login.html")

def inserttotable(request):
    print("Registration success")
    fname=request.POST.get("Firstname")
    print(fname)
    context={}
    context["name"]=fname
    return render(request, "students/home.html",context)

