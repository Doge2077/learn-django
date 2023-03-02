from django.shortcuts import *
from django.http import *
from django.urls import *
import json

def f_request(request):
    path = request.path
    return HttpResponse(path)


def f_string(request):
    # data = request.GET.get('name')
    data = request.GET.getlist('name')
    return HttpResponse(data)


def f_formdata(request):
    # data1 = request.POST.get('name')
    # data2 = request.POST.get('statu')
    # return HttpResponse([data1, data2])
    data = request.POST.getlist('name')
    return HttpResponse(data)


def f_jsondata(request):

    json_bytes = request.body
    print(json_bytes, type(json_bytes))

    json_str = json_bytes.decode()
    print(json_str, type(json_str))

    json_dir = json.loads(json_str)
    print(json_dir, type(json_dir))

    return HttpResponse(json_dir)


def f_image(request):

    file_name = request.FILES.get('image')
    # print(file_name)

    file_data = request.FILES.get('image').read()

    with open('apps/App_03/static/%s' % file_name, 'wb') as file:
        file.write(file_data)

    return HttpResponse('Upload success.')