from django.shortcuts import render
from django.views import View 

# Login page
class Login(View):
    def get(self, request):
        return render(request, 'registration/login.html')

class Profile(View):
    def get(self, request):
        return render(request, 'usuario.html')