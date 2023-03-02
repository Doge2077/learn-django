from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.urls import reverse


def test_page(request):
    text = 'Lys is a dog, App_01'

    return HttpResponse(text)


def test_page_num(request, num):
    text = "The num is %d" % num

    return HttpResponse(text)


def test_page_re(request):
    text = 'LYS is' \
           'a dog'

    return HttpResponse(text)


def reverse_path(request):
    r_path = reverse('App_01:a_p')
    return HttpResponse(r_path)


def turn_to(request):
    return redirect('https://www.lys2021.com')


def turn_to_rap(request):
    r_path = reverse('App_01:a_p')
    return redirect(r_path)


def static_hiiro(request):
    path = 'static/App_01/hiiro.jpg'
    return HttpResponse(path)


# def hiiro_photo(request):
#     path = reverse('App_01:a_p')
#     return redirect(path)

def hiiro_photo(request):
    return redirect('/static/App_01/hiiro.jpg')