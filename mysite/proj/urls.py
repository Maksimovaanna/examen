from django.urls import path
from . import views

app_name = 'proj'

urlpatterns = [
    path('plswork', views.plswork, name='plswork')
]