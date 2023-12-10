# auth/urls.py

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView


from django.urls import path
from .views import UserRegistrationView, MyTokenObtainPairView, GetAllUsers, AssignAdminApiView



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('register/', UserRegistrationView.as_view(), name='user-registration'),

    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/', GetAllUsers.as_view(), name='all_users'),
    path('assign-admin/', AssignAdminApiView.as_view(), name='assign-admin'),
]
