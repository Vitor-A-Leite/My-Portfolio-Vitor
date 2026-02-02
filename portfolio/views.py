from django.shortcuts import render
from .data import *

# Create your views here.
def home(request):
    return render(request, 'home.html', {'skills': skills, 'Profile': Profile, 'Contact': Profile['Contact'], 'Education': Education, 'Experience': Experience, 'SoftSkills': SoftSkills, 'Projects': Projects})

def projects(request):
    return render(request, 'projects.html', {'Projects': Projects, 'Contact': Profile['Contact']})