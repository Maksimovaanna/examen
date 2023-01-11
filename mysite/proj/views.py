from django.shortcuts import render
from django.http import HttpResponse
from .models import Test, ID
import sqlite3
# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

def plswork(request):
    query = Test.objects.all()
    query2 = ID.objects.all()
    print(request)
    return render(request, 'proj/index.html', {"Test":query}, {"ID":query2})

def mygod():
    connection = sqlite3.connect('db.sqlite3')
    print(connection)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM proj_test")
    records = cursor.fetchall()
    num = (len(records))
    return num