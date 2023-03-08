from django.contrib import admin
from App_07.models import *


# Register your models here.

# 注册
# admin.site.register(Vtb_info)
# admin.site.register(Ski_info_A)


# 以块的形式嵌入从表
class Ski_info_Admin(admin.StackedInline):
    model = Ski_info_A
    extra = 0

@admin.register(Vtb_info)
class Vtb_info_Admin(admin.ModelAdmin):
    list_per_page = 114  # 每一页显示 114 条数据，默认值为 100

    # 设置动作选项位置
    actions_on_top = False  # 默认该值为 True
    actions_on_bottom = True  # 默认该值为 False

    # 在 admin 中展示更多列数据
    list_display = ['vtb_name', 'vtb_price', 'vtb_exp',
                    'vtb_reborn', 'vtb_age', 'vtb_fire',
                    'vtb_image']

    # 在 admin 中添加过滤器
    list_filter = ['vtb_name', 'vtb_reborn']

    # 在 admin 中添加搜索框
    search_fields = ['vtb_name']

    # 设置 admin 中可修改的字段列表
    # fields = ['vtb_exp']

    # 以块的形式嵌入从表
    inlines = [Ski_info_Admin]


@admin.register(Ski_info_A)
class Ski_info_A_Admin(admin.ModelAdmin):
    list_per_page = 1919

    list_display = ['ski_name', 'ski_damage', 'show_vtb_name']
