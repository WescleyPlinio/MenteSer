from django.urls import path
from .views import Index, Tratamentos

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tratamentos/', Tratamentos.as_view(), name='tratamentos'),
]