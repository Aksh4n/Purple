from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    honors = Honor.objects.all()
    bloks = Blok.objects.all()
    foams = Foam.objects.all()
    tirches = Tirche.objects.all()
    projects = Project.objects.all()
    videos = Video.objects.all()
    return render(request, 'index.html' , {'honors':honors , 'projects':projects , 'videos':videos , 'bloks':bloks , 'foams':foams , 'tirches':tirches})