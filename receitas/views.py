from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "home.html", context=
                  {
                      'nome':'Receitas Django'
                  })



def sobre(request):
    return HttpResponse("Sobre nós")

def receita(request):
    return HttpResponse("As receitas")