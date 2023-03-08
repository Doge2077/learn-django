import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from App_07.models import *


class vtbs_info_view(View):
    # 查询所有 vtb 信息的接口
    def get(self, request):
        vtb_list = Vtb_info.objects.all()
        vtb_data = []
        # 遍历查询集
        for vtb in vtb_list:
            vtb_dict = {
                'name': vtb.vtb_name,
                'price': vtb.vtb_price,
                'exp': vtb.vtb_exp,
                'reborn': vtb.vtb_reborn,
                'age': vtb.vtb_age,
                'image': vtb.vtb_image.url if vtb.vtb_image \
                    else ' '
            }
            vtb_data.append(vtb_dict)

        return JsonResponse(vtb_data, safe=False)

    # 创建 vtb 的接口
    def post(self, request):
        json_bytes = request.body         # 获取从前端传入的请求数据
        json_str = json_bytes.decode()    # 把 bytes 类型的数据转换成字符串
        vtb_dict = json.loads(json_str)    # 将 json 字符串数据转换成字典

        vtb = Vtb_info.objects.create(
            vtb_name=vtb_dict['vtb_name'],
            vtb_price=vtb_dict['vtb_price'],
            vtb_exp=vtb_dict['vtb_exp'],
            vtb_reborn=vtb_dict['vtb_reborn'],
            vtb_age=vtb_dict['vtb_age'],
            vtb_image=vtb_dict['vtb_image'],
        )

        vtb_dict = {
            'name': vtb.vtb_name,
            'price': vtb.vtb_price,
            'exp': vtb.vtb_exp,
            'reborn': vtb.vtb_reborn,
            'age': vtb.vtb_age,
            'image': vtb.vtb_image.url if vtb.vtb_image \
                else ' '
        }
        return JsonResponse(vtb_dict, status=201)
