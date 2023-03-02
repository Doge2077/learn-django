from django.shortcuts import render
from django.http import *
from django.urls import *
import json


# Create your views here.


def f_cookies(request):
    response = HttpResponse('Cookies set successfully.')

    response.set_cookie(key='name', value='lys', max_age=600)

    return response


def r_cookies(request):
    info = request.COOKIES.get('name')

    return HttpResponse(info)


def d_cookies(request):
    response = HttpResponse('Cookies deleted.')

    response.delete_cookie('name')

    return response


def f_session(request):
    request.session['name'] = 'hiiro'
    request.session['sex'] = 'cat'

    request.session.set_expiry(value=600)

    return HttpResponse('Session set successfully')


def r_session(request):
    name = request.session.get('name')
    sex = request.session.get('sex')

    return HttpResponse([name, sex])


def d_session(request):
    request.session.flush()  # 删除所有的session的全部信息
    # request.session.clear()  # 删除所有的session的值的信息
    # del request.session['name']  # 删除session中指定的键与值

    return HttpResponse('Session deleted.')