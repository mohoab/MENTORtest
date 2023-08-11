from django.shortcuts import render
from template import *






def home(request):
    return render(request , 'root/index.html')

def trainers(request):
    return render(request , 'root/trainers.html')

def about(request):
    return render(request , 'root/about.html')


def contact(request):
    return render(request , 'root/contact.html')

