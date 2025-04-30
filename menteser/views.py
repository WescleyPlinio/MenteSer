from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 
from .models import Transtorno, Servico, ImagemIndex

# Index page
class Index(View):
    def get(self, request):
        imagens = ImagemIndex.objects.all()
        servicos = Servico.objects.all()
        context = {
            'imagens': imagens,
            'servicos': servicos
        }
        return render(request, 'index.html', context)
    
class Tratamentos(View):
    def get(self, request):
        transtornos = Transtorno.objects.all()
        context = {
            'transtornos': transtornos,
        }
        return render(request, 'tratamentos.html', context)