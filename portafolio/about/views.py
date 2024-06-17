from django.shortcuts import render
from .models import Course, Skills


# Create your views here.
def about(request):
    courses = Course.objects.all
    skills = Skills.objects.all

    context = {'courses': courses, 'skills': skills}

    return render(request, 'about/about.html', context)
