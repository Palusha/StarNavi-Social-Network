from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import UserActivitySerializer, UserCreationSerializer


class SignUpView(generics.CreateAPIView):
    serializer_class = UserCreationSerializer
    permission_classes = (AllowAny,)


class UserActivityView(generics.RetrieveAPIView):
    queryset = get_user_model()
    serializer_class = UserActivitySerializer
    permission_classes = (AllowAny,)
