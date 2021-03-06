from django.db import models
# import datetime
from django.utils import timezone

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="covers/about-us/")

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name_plural = "about us"


class Announcement(models.Model):
    heading = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    pub_date = models.DateTimeField(default=timezone.now)
    show_this = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ['-created',]

class AboutDesc(models.Model):
    special = models.BooleanField(default=True, unique=True)
    heading = models.CharField(max_length=50)
    description = models.TextField(max_length=150)

    def __str__(self):
        return self.heading