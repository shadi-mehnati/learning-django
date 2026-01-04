from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def conection(request):
    return HttpResponse('you can call with us by this phne number 1234567')

def info(request):
    return render(request,'aboutus/info.html')