from django.urls import path, re_path
from django.views.generic import RedirectView
from App_01 import views

urlpatterns = [
    path('page/', views.test_page, name='a_p'),
    path('page/<int:num>/', views.test_page_num),
    re_path(r'^page/\w{2}\d{3}/$', views.test_page_re),
    path('reverse/', views.reverse_path),
    path('turn/', views.turn_to),
    path('turn_p', views.turn_to_rap),
    path('hiiro/', views.hiiro_photo),
    # path('hiiro/', RedirectView.as_view(url='static/App_01/hiiro.jpg')),
]