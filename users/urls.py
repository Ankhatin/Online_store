from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import UserTokenObtainPairView, UserCreateView
from rest_framework.permissions import AllowAny, IsAuthenticated

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserTokenObtainPairView.as_view(permission_classes=[AllowAny]), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=[AllowAny]), name='token_refresh'),
    path('create/', UserCreateView.as_view(), name='user_create'),
]