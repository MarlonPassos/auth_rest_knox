from django.urls import path, include 
from knox.views import LogoutView 

from .views import UserAPIViewm, RegisterAPIView, LoginAPIView 

urlpatterns = [
    path('', include('knox.urls')),
    path('user', UserAPIViewm.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout',  LogoutView.as_view(), name='knox_logout')
]
