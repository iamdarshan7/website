from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutUs
# Create your views here.

class AboutUsTemplateView(TemplateView):
    template_name = 'about_us.html'

def aboutUsTemplateView(request):
    aboutDatas = AboutUs.objects.all()
    context = {
        "aboutDatas": aboutDatas,
    }
    return render(request, 'about_us.html', context)

class PromiseTemplateView(TemplateView):
    template_name = 'promise.html'    

class EventTemplateView(TemplateView):
    template_name = 'event.html'

class AnnouncementTemplateView(TemplateView):
    template_name = 'announcement.html'    
