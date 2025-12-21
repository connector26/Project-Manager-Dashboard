from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='projectdashboard'),
    path('viewnotifications.html', views.viewnotifications, name='viewnotifications'),
    path('profile.html', views.profile, name='profile'),
    path('assignedprojects.html', views.assignedprojects, name='assignedprojects'),
    path('assignedteam.html', views.assignedteam, name='assignedteam'),
]
