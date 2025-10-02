from django.shortcuts import render
from django.http import HttpResponse

def map(request):
    return render(request,'map.html')

def mall(request):
    return render(request,'phoenixmall.html')

def veg(request):
    return render(request,'geetham-veg.html')

def grt(request):
    return render(request,'grt.html')

def college(request):
    return render(request,'gurunanak.html')

def westin(request):
    return render(request,'westin.html')
