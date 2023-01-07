from django.shortcuts import render
from django.http import HttpResponse
from .models import Test
# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

def plswork(request):
    query = Test.objects.all()
    print(request)
    return render(request, 'proj/index.html', {"Test":query})