from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_number', 'referral_code', 'referred_by']


class ReferralCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)

