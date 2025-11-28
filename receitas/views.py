from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

a = "Senai"

def home(request):
    return render(request, "page/home.html", context={'nome':a})

def sobre(request):
    return HttpResponse("Sobre nóis")

def receita(request):
    return HttpResponse("As receitas")

