from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "user"

urlpatterns = [
    # 회원가입
    # path("register/", views.Registration.as_view(), name="register"),
    ## DRF
    path("register/", views.RegistrationAPIView.as_view(), name="register"),

    # 로그인
    # path("login/", views.Login.as_view(), name="login"),
    path("login/", views.LoginAPIView.as_view(), name="login"),

    # 로그아웃
    # path("logout/", views.Logout.as_view(), name="logout"),

    ## JWT
    path('api-token-auth/', TokenObtainPairView.as_view(), name='api-token-auth'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='api-token-refresh'),

    # 사용자 정보
    path('userinfo/', views.UserInfoAPIView.as_view(), name='userinfo'),
]