from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    return render (request, 'home.html')

class AboutPageView(TemplateView): # new
    template_name = 'about.html'

class WebinarPageView(TemplateView): # new
    template_name = 'webinar.html'    

class ConsultingPageView(TemplateView): # new
    template_name = 'consulting.html'         

class WorkPageView(TemplateView): # new
    template_name = 'work.html'