from django.contrib import admin
from .models import AboutUs, Announcement, AboutDesc

# Register your models here.

admin.site.register(AboutUs)
admin.site.register(Announcement)
admin.site.register(AboutDesc)