from django.shortcuts import render

from .models import Job

def home(request):

    jobs = Job.objects  # gets all the object from db for Job and returns it as python objects
    return render(request,'jobs/home.html', {'jobs':jobs})