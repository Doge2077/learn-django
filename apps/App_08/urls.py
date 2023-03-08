from django.urls import *
from App_08 import views

urlpatterns = [
    path('vtbs/', views.vtbs_info_view.as_view())
]