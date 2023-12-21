from django.urls import path
from django.views.generic import TemplateView

from django.urls import path
from .views import (
    RegistrationAPIView,
    CustomUserLoginView,
    CustomUserList,
    CustomUserUpdate,
    ChangePasswordAPIView,
    CustomUserTokenRefreshView,
)

urlpatterns = [
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('api/v1/auth/register/', RegistrationAPIView.as_view(), name='registration'),
    path('api/v1/auth/login/', CustomUserLoginView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/user-list/', CustomUserList.as_view(), name='user_list'),
    path('api/v1/auth/user-update/<int:pk>/', CustomUserUpdate.as_view(), name='user_update'),
    path('api/v1/auth/change-password/', ChangePasswordAPIView.as_view(), name='change_password'),
    path('api/v1/auth/token-refresh/', CustomUserTokenRefreshView.as_view(), name='token_refresh'),
]