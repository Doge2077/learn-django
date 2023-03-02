from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.urls import *


def test_page(reuqest):
    text = 'Lys is a dog, App_02'

    return HttpResponse(text)


def test_page_num(request, num):
    text = "The num is %d" % num

    return HttpResponse(text)


def test_page_re(request):
    text = 'LYS is' \
           'a dog'

    return HttpResponse(text)


def reverse_path(request):
    r_path = reverse('App_02:a_p')
    return HttpResponse(r_path)


def turn_to(request):
    return redirect('https://lys2021.com/classifications/')


def turn_to_rap(request):
    r_path = reverse('App_02:a_p')
    return redirect(r_path)