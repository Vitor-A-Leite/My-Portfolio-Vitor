from django.shortcuts import render
from .data import get_home_context, get_projects_context

# Create your views here.
def home(request):
    return render(request, "home.html", get_home_context())

def projects(request):
    return render(request, "projects.html", get_projects_context())
