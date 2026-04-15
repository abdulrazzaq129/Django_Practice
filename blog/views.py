from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hi, welcom to blog home')

def about(request):
    return HttpResponse('Hi, welcom to blog about')

# Create your views here.
