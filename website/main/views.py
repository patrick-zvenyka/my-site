from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    certification = Certification.objects.all()
    project = Project.objects.all()


    context = {
        'education': education,
        'experience': experience,
        'certification': certification,
        'project': project,
    }

    return render(request, 'main/home.html', context)