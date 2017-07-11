from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'password',
        )


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=100,
    )
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.VailidationError('Username already exist')
        return username

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords didn\'t match')
        return data

    def save(self, *args, **kwargs):
        user = User.objects.crate_user(
            username=self.validated_data.get('username', ''),
            password=self.validated_data.get('password1', ''),
        )
        return user

