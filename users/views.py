from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserSerializer, UserTokenObtainPairSerializer


class UserCreateView(generics.CreateAPIView):
    """
    Контроллер отвечает за создание в базе данных нового пользователя (model User)
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer

