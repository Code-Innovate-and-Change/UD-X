from django.urls import path
from .views import SignUpView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path("signup/", SignUpView.as_view(),name="signup"),
    path("token/refresh/", TokenRefreshView.as_view(),name="token_refresh"),
    path("login/", LoginView.as_view(), name="login"),
]

