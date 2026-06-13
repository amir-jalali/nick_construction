from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class PhoneTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'phone'


class PhoneTokenObtainPairView(TokenObtainPairView):
    serializer_class = PhoneTokenObtainPairSerializer

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    referrer_code = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('phone', 'password', 'first_name', 'last_name', 'national_code', 'referrer_code')

    def create(self, validated_data):
        referrer_code = validated_data.pop('referrer_code', None)
        referrer = None
        if referrer_code:
            try:
                referrer = User.objects.get(phone=referrer_code)
            except User.DoesNotExist:
                pass

        user = User.objects.create_user(
            username=validated_data['phone'],
            phone=validated_data['phone'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            national_code=validated_data['national_code'],
            referrer=referrer
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone', 'first_name', 'last_name', 'national_code',
                  'credit', 'address', 'birth_date', 'profile_image',
                  'is_verified', 'created_at')
        read_only_fields = ('phone', 'credit', 'is_verified', 'created_at')