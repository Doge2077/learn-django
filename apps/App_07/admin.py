from django.contrib import admin
from App_07.models import *


# Register your models here.

# 注册
# admin.site.register(Vtb_info)
# admin.site.register(Ski_info_A)

@admin.register(Vtb_info)
class Vtb_info_Admin(admin.ModelAdmin):
    list_per_page = 114  # 每一页显示 114 条数据，默认值为 100

    # 设置动作选项位置
    actions_on_top = False  # 默认该值为 True
    actions_on_bottom = True  # 默认该值为 False

    # 在 admin 中展示更多列数据
    list_display = ['vtb_name', 'vtb_price', 'vtb_exp',
                    'vtb_reborn', 'vtb_age', 'vtb_fire']


@admin.register(Ski_info_A)
class Ski_info_A_Admin(admin.ModelAdmin):
    list_per_page = 1919
