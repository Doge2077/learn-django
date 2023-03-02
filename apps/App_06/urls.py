from django.urls import *
from App_06 import views

urlpatterns = [
    path('page/', views.template_view.as_view()),
    path('info/', views.template_info.as_view()),
]