from django.urls import path
from .views import RegisterView, LoginView, protected_view
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("protected/", protected_view, name="protected"),  # New Protected Route
]
