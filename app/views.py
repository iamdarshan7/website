from django.shortcuts import render
from django.http import JsonResponse
from .forms import ApplicationFormData, ContactFormData
from .models import Countries, Cities, ProgramsType, University, FilterForm, Subject, FeedBackByStudent, ApplicationForm
from django.views.generic import TemplateView, DetailView
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.


# class add_data(TemplateView):
#     template_name = "index.html"
#     object_name = "feedbacks"
#     model = FeedBackByStudent

def add_data(request):
    feedbacks = FeedBackByStudent.objects.all()
    actual_uni_count = University.objects.count()
    actual_program_count = ProgramsType.objects.count()
    actual_subject_count = Subject.objects.count()
    actual_happy_student = ApplicationForm.objects.count()
    context = {
        "feedbacks": feedbacks,
        "actual_uni_count": actual_uni_count,
        "actual_program_count": actual_program_count,
        "actual_subject_count": actual_subject_count,
        "actual_happy_student": actual_happy_student,
    }
    return render(request, 'index.html', context)
    
# def add_data(request):
#     if request.method == "POST":
#         form = FormDatas(request.POST or None)
#         data = {}
#         if request.is_ajax():
#             if form.is_valid():
#                 form.save()
#                 data['status'] = 'ok! success'
#                 return JsonResponse(data)
#                 form = FormDatas()
#     else:
#         form = FormDatas()

#     context = {
#         'form': form,
#     }
#     return render(request, 'index.html', context)




class Contact(TemplateView):
    template_name = "contact.html"

class Search(TemplateView):
    template_name = "search_programs.html"

class FormDetail(TemplateView):
    template_name = "appliform.html"    



# Below are the views for filtering
def is_valid_queryparam(param):
    return param != '' and param is not None

def filterView(request):
    qs = FilterForm.objects.all()
    country = request.GET.get('country')
    city = request.GET.get('city')
    university = request.GET.get('university')
    program = request.GET.get('programName')
    subject = request.GET.get('subject')
    paginator = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if is_valid_queryparam(country) and country != "Choose...":
        qs = qs.filter(country__name=country)
    
    if is_valid_queryparam(city) and city != "Choose...":
        qs = qs.filter(city__name=city)
    
    if is_valid_queryparam(subject) and subject != 'Choose...':
        qs = qs.filter(subject__name=subject)

    if is_valid_queryparam(program) and program != 'Choose...':
        qs = qs.filter(program__name=program)  

    if is_valid_queryparam(university) and university != 'Choose...':
        qs = qs.filter(university__name=university)
    
    qs_count = qs.count()
    if qs_count == 0 or qs_count == 1:
        page_obj = ''

    context = {
        'queryset': qs,
        'countries': Countries.objects.all(),
        "cities": Cities.objects.all(),
        "subjects": Subject.objects.all(),
        "programs": ProgramsType.objects.all(),
        "university": University.objects.all(),
        "page_obj": page_obj
    }
    return render(request, 'search_programs.html', context)    


class FilterDetailView(DetailView):
    model = FilterForm
    context_object_name ='details'
    template_name = "search_details.html"



# def get_program_data(request):        
#     qs_val = list(FacultyData.objects.values())
#     return JsonResponse({"data": qs_val})

# def get_percentage_data(request):
#     qs_val = list(PercentageData.objects.values())
#     return JsonResponse({"data": qs_val})


# def hello(request):

#     return render(request, 'index.html')


# def create_post(request):
#     posts = Data.objects.all()
#     response_data = {}

#     if request.POST.get('action') == 'post':
#         name = request.POST.get('name')
#         email = request.POST.get('email')

#         response_data['name'] = name
#         response_data['email'] = email

#         Data.objects.create(
#             name= name,
#             email = email,
#             )
#         return JsonResponse(response_data)    

#     return render(request, 'index.html', {'posts':posts})  




# def add_data(request):
#     form = FormDatas(request.POST or None)
#     data = {}
#     if request.is_ajax():
#         if form.is_valid():
#             form.save()
#             data['status'] = 'ok'
#             return JsonResponse(data)
#     context = {
#         'form': form
#     }
#     return render(request, 'index.html', context)

# def add_another_data(request):
#     if request.method == "POST":
#         fm = AnotherFormDatas(requeest.POST)
#         if fm.is_valid():
#             fm.save()
#             fm = AnotherFormDatas()
#     else: 
#         fm = AnotherFormDatas()

#     return render(request, 'index.html', {'fm': fm})  


def applicationFormView(request):
    # success = False
    if request.method == "POST":
        form = ApplicationFormData(request.POST, request.FILES)
        if form.is_valid():
            form.save()   
            form = ApplicationFormData()
            # succcess = True
            messages.add_message(request, messages.INFO, "Thank You")
        else: 
            messages.add_message(request, messages.INFO, 'Please fill again')    
    else: 
        form = ApplicationFormData()
    # print(success)     

    return render(request, 'appliform.html', {"form": form})


def contactFormView(request):
    if request.method == "POST":
        form = ContactFormData(request.POST or None)
        if form.is_valid():
            form.save()
            form = ContactFormData()
    else:
        form = ContactFormData()
    return render(request, 'contact.html', {"form": form})            

# for handling 400 and 500 error


def handler404(request, exception):
    return render(request, '404-not-found.html')


def handler500(request):
    return render(request, '500-not-found.html')