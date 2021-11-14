from django.contrib import admin
from .models import ContactForm, ApplicationForm, Countries, Cities, Subject, ProgramsType, University, FilterForm, FeedBackByStudent, Consultancy,HomePageInfo
# Register your models here.

# admin.site.register(Data)
# admin.site.register(FacultyData)
# admin.site.register(PercentageData)
admin.site.register(HomePageInfo)
admin.site.register(FilterForm)
admin.site.register(Consultancy)
admin.site.register(University)
admin.site.register(ContactForm)
admin.site.register(ApplicationForm)
admin.site.register(Cities)
admin.site.register(Countries)
admin.site.register(Subject)
admin.site.register(ProgramsType)
admin.site.register(FeedBackByStudent)


# @admin.register(Data)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'email', 'phone']