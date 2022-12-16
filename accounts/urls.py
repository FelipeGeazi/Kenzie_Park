from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path("accounts/", views.RegisterView.as_view()),
    path("accounts/<int:account_id>/", views.AccountDetailView.as_view()),
    path("login/", jwt_views.TokenObtainPairView.as_view()),
    path("refresh/", jwt_views.TokenRefreshView.as_view()),
]
