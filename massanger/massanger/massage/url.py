from django.urls import path

from .views import RegisterAPI, LoginAPI,UserAPI,ProfileAPI

urlpatterns =[
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/Login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/profile', ProfileAPI.as_view()),
]