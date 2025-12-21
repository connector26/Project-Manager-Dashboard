from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin
# Create your views here.


def index(request):
    return render(request,'index.html')

def view_notifications(request):
     return render(request,'viewnotifications.html')
 

def profile(request):
    user_info = {
        'name': 'John Doe',
        'mobile': '123-456-7890',
        'email': 'john.doe@example.com',
        'details': 'This is a brief description about John Doe.',
        'profile_image': 'images/profile.jpg',  # Path to the image in static folder
    }
    return render(request, 'profile.html', user_info)
