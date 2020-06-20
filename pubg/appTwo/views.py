from django.shortcuts import render
# from django.views.generic import CreateView
from django.http import HttpResponse
# from .models import Person
# Create your views here.

def index(request):
    return render(request,'first_app/home.html')

def register(request):
    return render(request,'first_app/register.html')


# class PersonCreateView(CreateView):
#     model = Person
#     fields = ('name', 'email', 'job_title', 'bio')
