from django.urls import *
from App_09 import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # 不带 pk 参数的路由
    path('vtbs/', views.vtbs_info_view.as_view()),
    # 带 pk 参数的路由，需要正则匹配
    re_path(r'^vtb/(?P<pk>\d+)/$', views.vtb_info_view.as_view()),
]

