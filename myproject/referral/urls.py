from django.urls import path
from .views import AuthAPIView, VerifyCodeAPIView, UserProfileAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
   openapi.Info(
      title="API Title",
      default_version='v1',
      description="API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourcompany.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(AllowAny,),
)


urlpatterns = [
    path('auth/', AuthAPIView.as_view()),
    path('verify/', VerifyCodeAPIView.as_view()),
    path('profile/<int:pk>/', UserProfileAPIView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

