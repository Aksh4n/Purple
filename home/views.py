from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    honors = Honor.objects.all()
    projects = Project.objects.all()
    return render(request, 'index.html' , {'honors':honors , 'projects':projects})