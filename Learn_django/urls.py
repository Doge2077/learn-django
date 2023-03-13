"""Learn_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os.path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from django.views.static import serve
from rest_framework.documentation import include_docs_urls

from Learn_django import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/', include(('App_01.urls', 'App_01'), namespace='App_01')),
    path('app02/', include(('App_02.urls', 'App_02'), namespace='App_02')),
    # path('app01/', include('App_01.urls')),
    # path('app02/', include('App_02.urls')),
    path('app03/', include(('App_03.urls', 'App_03'), namespace='App_03')),
    path('app04/', include(('App_04.urls', 'App_04'), namespace='App_04')),
    path('app05/', include(('App_05.urls', 'App_05'), namespace='App_05')),
    path('app06/', include(('App_06.urls', 'App_06'), namespace='App_06')),
    path('app07/', include(('App_07.urls', 'App_07'), namespace='App_07')),
    path('app08/', include(('App_08.urls', 'App_08'), namespace='App_08')),
    path('app09/', include(('App_09.urls', 'App_09'), namespace='App_09')),

    # 自动生成接口 API
    path('docs/', include_docs_urls(title='Vtbers API')),

    # media 静态文件路由
    re_path(r'^media/(?P<path>.+)$', serve, {'document_root': settings.MEDIA_ROOT})
]
