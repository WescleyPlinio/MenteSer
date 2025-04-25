from django.shortcuts import render
from django.views import View 

class Profile(View):
    def get(self, request):
        return render(request, 'usuario.html')