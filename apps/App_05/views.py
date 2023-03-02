from django.shortcuts import render
from django.urls import *
from django.http import *
from django.utils.decorators import method_decorator
from django.views import View


def func_view(request):
    if request.method == 'GET':
        html = 'Function view by GET.'
        return HttpResponse(html)

    if request.method == 'POST':
        html = 'Function view by POST.'
        return HttpResponse(html)


class class_view(View):

    def get(self, request):
        html = 'Class view by GET.'
        return HttpResponse(html)

    def post(self, request):
        html = 'Class view by POST.'
        return HttpResponse(html)


def decorator_func(func):
    def decorator(request, *args, **kwargs):
        print('Self decorator function called')
        print('Path : %s' % request.path)
        return func(request, *args, **kwargs)

    return decorator


# @method_decorator(decorator_func, name='dispatch')  # 装饰所有的视图函数
# @method_decorator(decorator_func, name='get')  # 装饰指定的视图函数
class d_class_view(View):

    @method_decorator(decorator_func)  # 装饰指定视图
    def get(self, request):
        return HttpResponse('Decorated class view by GET.')

    def post(self, request):
        return HttpResponse('Decorated class view by POST.')
