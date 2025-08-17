from django.urls import path
from app.views import gallerydetails,signupdetails,logindetails,tokenrefresh
urlpatterns = [
    path('gallery',gallerydetails.as_view(),name="details"),
    path('signup',signupdetails.as_view(),name="signup"),
    path('login',logindetails.as_view(),name="login"),
    path('tokenrefresh',tokenrefresh.as_view(),name="tokenrefresh"),
]
