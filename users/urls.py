from django.urls import path
from .views import Login, Profile

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('profile/', Profile.as_view(), name='profile'),
]