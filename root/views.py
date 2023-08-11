from django.shortcuts import render
from template import *






def home(request):
    return render(request , 'root/index.html')
