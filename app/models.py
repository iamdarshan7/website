from django.db import models
import uuid
from django.urls import reverse
from django.core import validators
from .validators import validate_number
from ckeditor.fields import RichTextField


# Create your models here.

# class PercentageData(models.Model):
#     title = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title

# class FacultyData(models.Model):
#     title = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title

# class Data(models.Model):
#     name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     phone=models.CharField(max_length=10,null=True, validators=[validate_number])
    # program = models.ForeignKey(FacultyData, on_delete=models.CASCADE)
    # percentage = models.ForeignKey(PercentageData, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name

class Countries(models.Model):
    name = models.CharField("country_name", max_length=100)
    
    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name

class Cities(models.Model):
    name = models.CharField("city_name", max_length=100)    

    class Meta:
        verbose_name_plural = "cities"


    def __str__(self):
        return self.name  

class Subject(models.Model):
    name = models.CharField("subject_name", max_length=100)

    def __str__(self):
        return self.name

class ProgramsType(models.Model):
    name = models.CharField("program_name", max_length=100)
    duration = models.IntegerField()
    requirement_1 = models.CharField(max_length=200)
    requirement_2 = models.CharField(max_length=200)
    requirement_3 = models.CharField(max_length=200)
    requirement_4 = models.CharField(max_length=200)
    requirement_5 = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class University(models.Model):
    name = models.CharField("university_name", max_length=100)
    cover_photo = models.ImageField(upload_to="covers/uni_cover_photo/")
    uni_logo =  models.ImageField(upload_to="covers/uni_logo/")
    desc = RichTextField("uni_short_description")
    fee = models.IntegerField()
    desc_1 = RichTextField("uni_long_paragraph_description")
    summer_intake_date = models.DateField(blank=True, null=True)
    winter_intake_date = models.DateField(blank=True, null=True)

    class Meta: 
        verbose_name_plural = "universities"
    
    def __str__(self):
        return  self.name

class FilterForm(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    program = models.ForeignKey(ProgramsType, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("search_detail", args=[str(self.id)])    


class ApplicationForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone=models.CharField(max_length=10,null=True, validators=[validate_number])  
    college = models.ForeignKey(University, on_delete=models.CASCADE)
    program = models.ForeignKey(ProgramsType, on_delete=models.CASCADE)
    files = models.FileField(upload_to="covers/")

    def __str__(self):
        return self.first_name


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone= models.CharField(max_length=10,null=True, validators=[validate_number])  
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name



# feedback model by students
class FeedBackByStudent(models.Model):
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    feedback = models.TextField(max_length=100)
    image = models.ImageField(upload_to="covers/feedback/")

    def __str__(self):
        return self.name