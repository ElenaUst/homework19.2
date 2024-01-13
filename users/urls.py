from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, generate_new_password,\
    VerificationFailedView, activate

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword', generate_new_password, name='generate_new_password'),
    path('activate/<str:uidb64>/<str:token>/>', activate, name='activate'),
    path('verification_failed/', VerificationFailedView.as_view(), name='verification_failed'),

]