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
    name = models.CharField("country_name", max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name

class Cities(models.Model):
    name = models.CharField("city_name", max_length=100, unique=True)    

    class Meta:
        verbose_name_plural = "cities"


    def __str__(self):
        return self.name  

class Subject(models.Model):
    name = models.CharField("subject_name", max_length=100, unique=True)

    def __str__(self):
        return self.name

class ProgramsType(models.Model):
    name = models.CharField("program_name", max_length=100, unique=True)
    # duration = models.IntegerField()
    # requirement_1 = models.CharField(max_length=200)
    # requirement_2 = models.CharField(max_length=200)
    # requirement_3 = models.CharField(max_length=200)
    # requirement_4 = models.CharField(max_length=200)
    # requirement_5 = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class University(models.Model):
    name = models.CharField("university_name", max_length=100, unique=True)
    cover_photo = models.ImageField(upload_to="covers/uni_cover_photo/")
    uni_logo =  models.ImageField(upload_to="covers/uni_logo/")
    desc = models.TextField("uni_short_description", max_length=100)
    special = models.BooleanField(default=False)
    website_link = models.URLField(blank=True, null=True)
    # fee = models.IntegerField()
    # desc_1 = RichTextField("uni_long_paragraph_description")
    # summer_intake_date = models.DateField(blank=True, null=True)
    # winter_intake_date = models.DateField(blank=True, null=True)

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
    # name = models.CharField(max_length=100)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    program = models.ForeignKey(ProgramsType, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    fee = models.CharField("Fee: Write with Rs or $ before actual Fee",max_length=10, default='N/A')
    desc_1 = RichTextField("program_long_paragraph_description")
    summer_intake_date = models.DateField(blank=True, null=True)
    winter_intake_date = models.DateField(blank=True, null=True)

    duration = models.CharField("Duration: Eg. 2 or 2.5 ", max_length=6)
    requirement_1 = models.CharField(max_length=200)
    requirement_2 = models.CharField(max_length=200)
    requirement_3 = models.CharField(max_length=200)
    requirement_4 = models.CharField(max_length=200)
    requirement_5 = models.CharField(max_length=200)

    class Meta:
        unique_together = (('university', 'program'),)

    def __str__(self):
        return f"{self.university} with {self.program}"

    def get_absolute_url(self):
        return reverse("search_detail", args=[str(self.id)])    


class ApplicationForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone=models.CharField(max_length=10,null=True, validators=[validate_number])  
    college = models.ForeignKey(University, on_delete=models.CASCADE)
    program = models.ForeignKey(ProgramsType, on_delete=models.CASCADE)
    files = models.FileField(upload_to="covers/application_file/")

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
    show_this = models.BooleanField(default=True)
    image = models.ImageField(upload_to="covers/feedback/")

    def __str__(self):
        return self.name

class Consultancy(models.Model):
    name = models.CharField("consultancy_name", max_length=100)
    logo_photo = models.ImageField(upload_to='covers/consultancy/')
    desc = models.TextField(max_length=200)
    special = models.BooleanField(default=False)
    website_link = models.URLField(blank=True, null=True)


    def __str__(self):
        return  self.name

    class Meta: 
        verbose_name_plural = "consultancies"

class HomePageInfo(models.Model):
    special = models.BooleanField(default=True, unique=True)
    moto = models.CharField("company_moto", max_length=100)
    heading_title = models.CharField("Heading_title", max_length=100)
    heading_first_image = models.ImageField("HomePage_background_image1",upload_to='covers/homepage/')
    heading_second_image = models.ImageField("HomePage_background_image2",upload_to='covers/homepage/')
    button_name1 = models.CharField("study_program_button", max_length=100)
    button_name2 = models.CharField("talk_to_us_button", max_length=100)

    apply_online_title = models.CharField("Apply_online_title", max_length=100)
    apply_online_desc = models.CharField("Apply_online_desc", max_length=100)
    apply_online_button_name = models.CharField("Apply_online_button_name", max_length=100)

    contact_us_title = models.CharField("contact_us_title", max_length=100)
    contact_us_desc = models.CharField("contact_us_desc", max_length=100)
    contact_us_button_name = models.CharField("contact_us_button_name", max_length=100)

    feature_title = models.CharField("Feature_title", max_length=100)
    feature_heading_title = models.CharField("Feature_heading_title", max_length=100)
    
    stats_title = models.CharField("Stats_Title", max_length=100)
    stats_image = models.ImageField("Stats_background_image" ,upload_to='covers/homepage/')


    article_title = models.CharField("Articles_by_Students_title", max_length=100)
    # article_image = models.ImageField("Article_background_image",upload_to='covers/homepage/')

    def __str__(self):
        return self.moto