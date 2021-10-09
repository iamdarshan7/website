from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutUs, Announcement
from app.models import ApplicationForm
# Create your views here.

class AboutUsTemplateView(TemplateView):
    template_name = 'about_us.html'

def aboutUsTemplateView(request):
    aboutDatas = AboutUs.objects.all()
    actual_happy_student = ApplicationForm.objects.count()

    context = {
        "aboutDatas": aboutDatas,
        "actual_happy_student": actual_happy_student,
    }
    return render(request, 'about_us.html', context)

class PromiseTemplateView(TemplateView):
    template_name = 'promise.html'    

class EventTemplateView(TemplateView):
    template_name = 'event.html'

# class AnnouncementTemplateView(TemplateView):
#     template_name = 'announcement.html'    

def announcementTemplateView(request):
    announceDatas = Announcement.objects.all()
    context = {
        "announceDatas": announceDatas,
    }
    return render(request, 'announcement.html', context)
