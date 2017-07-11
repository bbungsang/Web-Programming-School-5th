from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions

from member.permissions import ObjectIsRquestUser
from member.serializers.user import UserSerializer

User = get_user_model()


class UserListCreateView(generics.ListAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        elif self.request.method == 'POST':
            return UserCreateSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        ObjectIsRquestUser,
    )