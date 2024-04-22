from django.urls import path
from .views import AuthAPIView, VerifyCodeAPIView, UserProfileAPIView, AuthTemplateView, VerifyCodeTemplateView, UserProfileTemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

app_name = 'referral'


schema_view = get_schema_view(
   openapi.Info(
      title="API Реферальной Системы",
      default_version='v1',
      description="Этот API управляет реферальной системой с функциональностью, включающей аутентификацию по номеру телефона, управление профилем и обработку реферальных кодов. Пользователи могут регистрироваться, входить в систему, используя свой номер телефона, получать автоматически генерируемый 6-значный пригласительный код и использовать пригласительный код другого пользователя для связывания профилей.",
      terms_of_service="https://github.com/melixz/ReferNet",
      contact=openapi.Contact(email="dr.melix@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # API Endpoints
    path('api/auth/', AuthAPIView.as_view(), name='api-auth'),
    path('api/verify/', VerifyCodeAPIView.as_view(), name='api-verify'),
    path('api/profile/<int:pk>/', UserProfileAPIView.as_view(), name='api-profile'),

    # Template Views for Testing
    path('auth/', AuthTemplateView.as_view(), name='auth'),
    path('verify/', VerifyCodeTemplateView.as_view(), name='verify-code'),
    path('profile/<int:pk>/', UserProfileTemplateView.as_view(), name='user-profile'),

    # Documentation URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]