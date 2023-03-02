from django.urls import *
from App_05 import views

urlpatterns = [
    path('fview/', views.func_view),
    path('cview/', views.class_view.as_view()),
    path('dcview/', views.d_class_view.as_view()),
]