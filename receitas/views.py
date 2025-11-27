from django.shortcuts import render


# Create your views here.

a = "Senai"

def home(request):
    return render(request, "home.html", context={'nome':a})