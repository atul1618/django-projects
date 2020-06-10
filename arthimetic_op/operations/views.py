from django.shortcuts import render


# Create your views here.

def addition(request):
    return render(request,"addition/add_num.html")

def addresult(request):
    firstnum=int(request.POST.get("num1"))
    secondnum=int(request.POST.get("num2"))
    res= firstnum + secondnum
    context={}
    context["opresult1"]=res
    return render(request,"result/addition_results.html",context)

def subtract(request):
    return render(request,"subtraction/sub_num.html")

def subresult(request):
    firstnum = int(request.POST.get("num1"))
    secondnum = int(request.POST.get("num2"))
    res = firstnum - secondnum
    context = {}
    context["opresult2"] = res
    return render(request, "result/subtraction_results.html", context)

def multiply(request):
    return render(request,"multiplication/mul_num.html")

def mulresult(request):
    firstnum = int(request.POST.get("num1"))
    secondnum = int(request.POST.get("num2"))
    res = firstnum * secondnum
    context = {}
    context["opresult3"] = res
    return render(request, "result/multiplication_results.html", context)


def divide(request):
    return render(request,"division/div_num.html")

def divresult(request):
    firstnum = int(request.POST.get("num1"))
    secondnum = int(request.POST.get("num2"))
    res = firstnum / secondnum
    context = {}
    context["opresult4"] = res
    return render(request, "result/division_results.html", context)


