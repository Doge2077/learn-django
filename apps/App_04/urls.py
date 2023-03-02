from django.urls import *
from App_04 import views

urlpatterns = [
    path('set_cookie/', views.f_cookies),
    path('read_cookie/', views.r_cookies),
    path('del_cookie/', views.d_cookies),
    path('set_session/', views.f_session),
    path('read_session/', views.r_session),
    path('del_session/', views.d_session),
]