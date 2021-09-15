from django.shortcuts import render
from django.http import HttpResponse
from .models import News
from http import *
# Create your views here.
def index(request):
    news= News.objects.all()
    return render(request,'news/index.html',{'news':news,'title':"Список новостей"})

