from . import views
from django.urls import path


urlpatterns = [
    path('', views.add_data.as_view(), name='add'),
    path('appform_detail/', views.applicationFormView, name="AppFormDetail"),
    path("search/", views.filterView, name="search"),
    path("search/<uuid:pk>/", views.FilterDetailView.as_view(), name="search_detail"),
    path('contact/', views.contactFormView, name="contact_page"),
    # path('', views.hello, name='hello'),
    # path('another/', views.add_another_data, name="add_another"),
    # path('program-data/', views.get_program_data, name='program-data'),
    # path('percentage-data/', views.get_percentage_data, name='percentage-data'),
]
