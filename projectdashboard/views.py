from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin
# Create your views here.


def index(request):
    return render(request,'index.html')

def viewnotifications(request):
    return render(request,'viewnotifications.html')
 

def profile(request):
    return render(request, 'profile.html')

def assignedprojects(request):
    return render(request, 'assignedprojects.html')

def assignedteam(request):
    return render(request, 'assignedteam.html')
