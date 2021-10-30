from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutUs, Announcement, AboutDesc
from app.models import ApplicationForm
from datetime import date
from app.models import University, Consultancy
# Create your views here.

# Helper function
def incrementPeopleWithEachYear(request, tyd, expYear):
    this_day = date.today()
    new_year = this_day.year
    diff = new_year - tyd
    expYear = expYear + diff
    return expYear

class AboutUsTemplateView(TemplateView):
    template_name = 'about_us.html'

def aboutUsTemplateView(request):
    aboutDatas = AboutUs.objects.all()
    actual_happy_student = ApplicationForm.objects.count()
    aboutDesc = AboutDesc.objects.filter(special=True)

    #for year of experience
    tyd = 2021
    expYear = 5
    days_of_experience = incrementPeopleWithEachYear(request, tyd, expYear)

    #for associate partners
    special_uni = University.objects.filter(special=True).count()
    special_consultancy = Consultancy.objects.filter(special=True).count()
    associate_partner = special_uni + special_consultancy

    context = {
        "aboutDatas": aboutDatas,
        "actual_happy_student": actual_happy_student,
        "days_of_experience": days_of_experience,
        "associate_partner": associate_partner,
        "aboutDesc":aboutDesc,
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
