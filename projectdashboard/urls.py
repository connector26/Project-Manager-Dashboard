from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="projectdashboard"),
    path('viewnotifications.html',views.view_notifications,name="viewnotifications"),
    path('profile.html',views.profile,name="profile"),
    
]
