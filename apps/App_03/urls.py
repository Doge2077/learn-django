from django.urls import *
from App_03 import views

urlpatterns = [
    path('request/', views.f_request),
    path('findstr/', views.f_string),
    path('formdata/', views.f_formdata),
    path('jsondata/', views.f_jsondata),
    path('image/', views.f_image),
]