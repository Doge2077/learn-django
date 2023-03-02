from django.shortcuts import render
from django.http import *
from django.template import loader
from django.views import View


# Create your views here.


class template_view(View):

    def get(self, request):
        # template = loader.get_template('index.html')
        args = {'name': 'lys', 'hiiro': 'debu cat'}

        return render(request, 'index.html', args)


class template_info(View):

    def get(self, request):
        # template = loader.get_template('index.html')
        args = {
            'name': 'Lys',
            'info': {
                'blog': 'lys2021.com',
                'status': 'liveable',
                'age': '114514',
            }
        }
        return render(request, 'info.html', args)
