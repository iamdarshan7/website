from django import forms
from .models import ApplicationForm, ContactForm

# class FormDatas(forms.ModelForm):
#     class Meta:
#         model = Data
#         fields = ('name', 'email', 'phone')
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'name':'dzother[Name]','id':'id_name'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address', 'name': 'dzother[Email]','id':'id_email'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone', 'name': 'dzother[Phone]','id':'id_phone'}),
#         }


# class AnotherFormDatas(forms.ModelForm):
#     class Meta:
#         model = AnotherData
#         fields = ('location', 'stream', 'college', 'university')        


class ApplicationFormData(forms.ModelForm):

    class Meta:
        model = ApplicationForm
        fields = ("first_name", 'last_name', "email", "phone", 'college', "program", "files")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control ", "type": "text", "placeholder": "", "id": "id_first_name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control ", "type": "text", "placeholder": "", "id": "id_last_name"}),
            "email": forms.EmailInput(attrs={"class": "form-control ", "type": "email", "placeholder": "", "id": "id_email"}),
            "phone": forms.TextInput(attrs={"class": "form-control ", "type": "text", "placeholder": "", "id": "id_phone"}),
            "college": forms.Select(attrs={"class": "form-control ", "type": "select", "placeholder": "", "id": "id_college"}),
            "program": forms.Select(attrs={"class": "form-control ", "type": "select", "placeholder": "", "id": "id_program"}),
            "files": forms.FileInput(attrs={"placeholder": "", "type": "file", "id": "id_files"}),
        }

class ContactFormData(forms.ModelForm):
    
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'phone', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'name':'dzother[Name]','id':'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address', 'name': 'dzother[Email]','id':'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone', 'name': 'dzother[Phone]','id':'phone'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject', 'name': 'dzother[Subject]','id':'subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message..', 'rows':'4' , 'name': 'message','id':'message'}),
        }
