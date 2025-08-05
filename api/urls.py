from django.urls import path
from app.views import userdata,signup

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("userdata",userdata.as_view(),name="userdata"),
    path("signup",signup.as_view(),name="signup"),

    path('login', TokenObtainPairView.as_view(), name='login'),  
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

]