import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from App_07.models import *


# # 不带参数
# class vtbs_info_view(View):
#     # 查询所有 vtb 信息的接口
#     def get(self, request):
#         vtb_list = Vtb_info.objects.all()
#         vtb_data = []
#         # 遍历查询集
#         for vtb in vtb_list:
#             vtb_dict = {
#                 'name': vtb.vtb_name,
#                 'price': vtb.vtb_price,
#                 'exp': vtb.vtb_exp,
#                 'reborn': vtb.vtb_reborn,
#                 'age': vtb.vtb_age,
#                 'image': vtb.vtb_image.url if vtb.vtb_image \
#                     else ' '
#             }
#             vtb_data.append(vtb_dict)
#
#         return JsonResponse(vtb_data, safe=False)
#
#     # 创建 vtb 的接口
#     def post(self, request):
#         json_bytes = request.body  # 获取从前端传入的请求数据
#         json_str = json_bytes.decode()  # 把 bytes 类型的数据转换成字符串
#         vtb_dict = json.loads(json_str)  # 将 json 字符串数据转换成字典
#
#         vtb = Vtb_info.objects.create(
#             vtb_name=vtb_dict['vtb_name'],
#             vtb_price=vtb_dict['vtb_price'],
#             vtb_exp=vtb_dict['vtb_exp'],
#             vtb_reborn=vtb_dict['vtb_reborn'],
#             vtb_age=vtb_dict['vtb_age'],
#             vtb_image=vtb_dict['vtb_image'],
#         )
#
#         vtb_dict = {
#             'name': vtb.vtb_name,
#             'price': vtb.vtb_price,
#             'exp': vtb.vtb_exp,
#             'reborn': vtb.vtb_reborn,
#             'age': vtb.vtb_age,
#             'image': vtb.vtb_image.url if vtb.vtb_image \
#                 else ' '
#         }
#         return JsonResponse(vtb_dict, status=201)
#
#
# # 带参数
# class vtb_info_view(View):
#     # 查询 vtb 的接口
#     def get(self, request, pk):
#         try:
#             # 查询与 pk 值对应编号 id 的英雄信息
#             vtb = Vtb_info.objects.get(id=pk)
#         except Vtb_info.DoesNotExist:
#             return HttpResponse({"message": "Vtb not found."}, status=404)
#
#         vtb_dict = {
#             'name': vtb.vtb_name,
#             'price': vtb.vtb_price,
#             'exp': vtb.vtb_exp,
#             'reborn': vtb.vtb_reborn,
#             'age': vtb.vtb_age,
#             'image': vtb.vtb_image.url if vtb.vtb_image \
#                 else ' '
#         }
#
#         return JsonResponse(vtb_dict, status=201)
#
#     # 修改 vtb 的接口
#     def put(self, request, pk):
#         try:
#             # 查询与 pk 值对应编号 id 的英雄信息
#             vtb = Vtb_info.objects.get(id=pk)
#         except Vtb_info.DoesNotExist:
#             return HttpResponse({"message": "Vtb not found."}, status=404)
#
#         # 获取 vtb 数据
#         json_bytes = request.body  # 获取从前端传入的请求数据
#         json_str = json_bytes.decode()  # 把 bytes 类型的数据转换成字符串
#         vtb_dict = json.loads(json_str)  # 将 json 字符串数据转换成字典
#
#         # 修改 vtb 数据
#         vtb.vtb_name = vtb_dict['vtb_name']
#         vtb.vtb_price = vtb_dict['vtb_price']
#         vtb.vtb_exp = vtb_dict['vtb_exp']
#         vtb.vtb_reborn = vtb_dict['vtb_reborn']
#         vtb.vtb_age = vtb_dict['vtb_age']
#         vtb.vtb_image = vtb_dict['vtb_image']
#         vtb.save()
#
#         json_dict = {
#             'name': vtb.vtb_name,
#             'price': vtb.vtb_price,
#             'exp': vtb.vtb_exp,
#             'reborn': vtb.vtb_reborn,
#             'age': vtb.vtb_age,
#             'image': vtb.vtb_image.url if vtb.vtb_image \
#                 else ' '
#         }
#
#         return JsonResponse(json_dict)
#
#     def delete(self, request, pk):
#         try:
#             # 查询与 pk 值对应编号 id 的英雄信息
#             vtb = Vtb_info.objects.get(id=pk)
#         except Vtb_info.DoesNotExist:
#             return HttpResponse({"message": "Vtb not found."}, status=404)
#
#         vtb.delete()  # 物理删除，无法恢复
#         # vtb.is_delete = True  # 逻辑删除，还有数据
#         return HttpResponse("Vtb deleted.", status=204)  # 需要指定状态码为 204


from rest_framework.viewsets import ModelViewSet  # 导入视图集
from App_08.serializers import vtb_info_serializers  # 导入序列化器


# 使用 DRF 框架编写的视图类
class vtb_drf_view(ModelViewSet):
    queryset = Vtb_info.objects.all()            # 查询所有的英雄信息
    serializer_class = vtb_info_serializers      # 使用序列化器对英雄信息进行序列化（格式转换）


