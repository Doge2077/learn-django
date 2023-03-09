from django.urls import *
from App_08 import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # # 不带 pk 参数的路由
    # path('vtbs/', views.vtbs_info_view.as_view()),
    # # 带 pk 参数的路由，需要正则匹配
    # re_path(r'^vtb/(?P<pk>\d+)/$', views.vtb_info_view.as_view()),
]

# DRF 框架路由的定义
router = DefaultRouter()  # 定义可以处理的视图类
router.register(r'vtbs', views.vtb_drf_view, basename='vtbers')  # 向路由器中注册视图集，并起别名

urlpatterns += router.urls  # 将路由器中的所有路由信息追加到 Django 的路由列表
