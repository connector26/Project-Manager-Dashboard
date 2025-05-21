from .views import RegistrationView
from .views import UsernameValidationView
from .views import EmailValidationView
from .views import EmailValidationView
from .views import VerificationView
from .views import LoginView
from .views import LogoutView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt,csrf_protect


urlpatterns = [
    path('register',RegistrationView.as_view(),name="register"),
    path('login',LoginView.as_view(),name="login"),
    path('validate-username',csrf_exempt(UsernameValidationView.as_view()),
    name="validate-username"),
    path('validate-email',csrf_exempt(EmailValidationView.as_view()),name='validate_email'),
    
    path('activate/<uidb64>/<token>',VerificationView.as_view(),name="activate"),
    path('logout',LogoutView.as_view(),name="logout"),
    
    
    
]
