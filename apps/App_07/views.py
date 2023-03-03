from django.shortcuts import render
from django.views import View
from django.http import *
from App_07.models import *


# 数据库增删改查
class db_view(View):
    # 新增vtb
    def post(self, request):
        # 新增 vtb_info
        # vtb = Vtb_info(vtb_name='Liiys',
        #                vtb_price=999999999.99,
        #                vtb_exp=0,
        #                vtb_reborn=True,
        #                vtb_age='2002-3-30',
        #                )
        # # 保存实例化对象
        # vtb.save()
        Vtb_info.objects.create(
            vtb_name='Liiys',
            vtb_price=999999999.99,
            vtb_exp=0,
            vtb_reborn=True,
            vtb_age='2002-3-30',
        )
        # 此方式创建无需保存 推荐使用

        return HttpResponse('New vtb bron.')

    # vtb 数据修改
    def put(self, request):
        # 第一种修改方式：
        # # 1. 先找到需要修改的对象
        # vtb = Vtb_info.objects.get(id=2)
        # # 2. 修改信息
        # vtb.vtb_name, vtb.vtb_price = 'LYS', 114514
        # # 3. 保存修改
        # vtb.save()

        # 第二种修改方式：
        # 在视图函数中添加如下代码
        Vtb_info.objects.filter(id=3).update(vtb_name='Lys', vtb_price=1919)

        return HttpResponse('Modify vtb data.')

    # vtb 数据删除
    def delete(self, request):
        # 第一种删除方式：
        # vtb = Vtb_info.objects.get(id=5)
        # vtb.delete()

        # 第二种删除方式：
        Vtb_info.objects.get(id=7).delete()
        return HttpResponse('Vtb deleted.')

    # vtb 数据查询
    def get(self, request):
        # 基本查询L:
        # 第一种查询方式 get 查询单一对象，如果不存在或者有多个会抛异常
        # vtb = Vtb_info.objects.get(id=1)
        # print(vtb)

        # 第二种查询方式 all 查询全部结果，返回一个 QuerySet 查询集列表
        # vtb = Vtb_info.objects.all()
        # print(vtb)

        # 第三种查询方式 count 查询结果数量
        # print(Vtb_info.objects.count())

        # 过滤查询：
        # 以 filter 为例子



        return HttpResponse('Vtb found.')