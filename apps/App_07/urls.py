from django.urls import *
from App_07 import views

urlpatterns = [
    path('db/', views.db_view.as_view()),
]