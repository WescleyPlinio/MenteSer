from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 

# Index page
class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    
class Tratamentos(View):
    def get(self, request):
        return render(request, 'tratamentos.html')