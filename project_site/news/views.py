from django.shortcuts import render
from django.http import HttpResponse
from http import *
# Create your views here.
def index(request):
    print(request)
    return HttpResponse()
def test(request):


    return HttpResponse("Hello")
