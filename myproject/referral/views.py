from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView
from .models import User
from .serializers import UserSerializer
import time


class AuthAPIView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        # ... Логика проверки и отправки кода
        time.sleep(1)  # Имитация задержки отправки
        return Response(status=status.HTTP_200_OK)


class VerifyCodeAPIView(APIView):
    def post(self, request):
        code = request.data.get('code')
        # ... Логика верификации кода и создания/получения пользователя
        return Response(status=status.HTTP_200_OK)


class UserProfileAPIView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class AuthTemplateView(TemplateView):
    template_name = 'referral/auth.html'


class VerifyCodeTemplateView(TemplateView):
    template_name = 'referral/verify_code.html'


class UserProfileTemplateView(TemplateView):
    template_name = 'referral/user_profile.html'