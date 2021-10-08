from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="covers/about-us/")

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name_plural = "about us"