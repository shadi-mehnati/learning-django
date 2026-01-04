from django.shortcuts import render
from django.http import HttpResponse

def production(request):
    return HttpResponse('we have many productions')
def pants(request):
    return render(request,"products/pants.html")
def shirt(request):
    return HttpResponse("they are in blue ,pink,red")
