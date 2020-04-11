from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithColorView, CustomUserCreateView, HelloWorldView

urlpatterns = [
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', CustomUserCreateView.as_view(), name='create_user'),
    path('hello_world/', HelloWorldView.as_view(), name='hello_world'),    
]
