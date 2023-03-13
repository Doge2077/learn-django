from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from App_07.models import Vtb_info
from App_08.serializers import *


# APIView
class vtbs_info_view(APIView):
    # 查询所有 vtb 信息的接口
    def get(self, request):
        # 查询所有的 vtb 信息
        vtb_list = Vtb_info.objects.all()

        # 使用序列化器自动转格式
        vtbs = vtb_info_serializers(vtb_list, many=True)

        # 将序列化后的数据响应给前端
        return Response(vtbs.data)

    # 创建 vtb 的接口
    def post(self, request):
        # DRF 接口解析
        # 获取前端所有数据
        vtb_data = request.data
        # 将数据反序列化
        vtbs = vtb_info_serializers(data=vtb_data)
        # 验证反序列化后的数据
        vtbs.is_valid(raise_exception=True)
        # 保存数据
        vtbs.save()
        # 视图响应
        return JsonResponse(vtbs.data, status=status.HTTP_201_CREATED)


# 带参数
class vtb_info_view(APIView):
    # 查询 vtb 的接口
    def get(self, request, pk):
        try:
            # 查询与 pk 值对应编号 id 的英雄信息
            vtb = Vtb_info.objects.get(id=pk)
        except Vtb_info.DoesNotExist:
            # 未查询到返回 404
            return Response(status.HTTP_404_NOT_FOUND)

        # 将查询到的 vtb 数据进行序列化，并转换为字典格式
        vtbs = vtb_info_serializers(instance=vtb)

        return Response(vtbs.data, status=201)

    # 修改 vtb 的接口
    def put(self, request, pk):
        try:
            # 查询与 pk 值对应编号 id 的英雄信息
            vtb = Vtb_info.objects.get(id=pk)
        except Vtb_info.DoesNotExist:
            # 未查询到返回 404
            return Response(status.HTTP_404_NOT_FOUND)

        # 解析前端传入的 json 数据
        vtb_data = request.data
        # 将 json 数据反序列化
        vtbs = vtb_info_serializers(instance=vtb, data=vtb_data)
        # 将反序列化后的数据进行验证
        vtbs.is_valid(raise_exception=True)
        # 保存数据
        vtbs.save()

        return Response(vtbs.data)

    # 删除 vtb 的接口
    def delete(self, request, pk):
        try:
            # 查询与 pk 值对应编号 id 的英雄信息
            vtb = Vtb_info.objects.get(id=pk)
        except Vtb_info.DoesNotExist:
            # 未查询到返回 404
            return Response(status.HTTP_404_NOT_FOUND)

        vtb.delete()  # 物理删除，无法恢复
        # vtb.is_delete = True  # 逻辑删除，还有数据
        return Response("Vtb deleted.", status=204)  # 需要指定状态码为 204
