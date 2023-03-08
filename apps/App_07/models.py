from django.db import models


# 定义信息类 Vtb_info
class Vtb_info(models.Model):
    # 类的属性（表的字段）
    vtb_name = models.CharField(max_length=114, default='Hiiro', verbose_name='名称')
    vtb_price = models.FloatField(default=114514.1919, verbose_name='价格')
    vtb_exp = models.IntegerField(default=233, verbose_name='次数')
    vtb_reborn = models.BooleanField(default=False, verbose_name='转生')
    vtb_age = models.DateField(verbose_name='时间', auto_now_add=True)
    vtb_image = models.ImageField(upload_to='vtb_image', verbose_name='头像', null=True)

    # 元属性
    class Meta:
        db_table = 'vtb_info'  # 指定数据库中的表的名称 非中文
        verbose_name = 'Vtb名称'  # 指定表的别名 可以为中文
        verbose_name_plural = verbose_name  # 指定复数形式也为别名

    def __str__(self):
        return self.vtb_name  # 一般返回名称

    # 手写一个展示列的方法，将方法作为列来展示
    def vtb_fire(self):
        if self.vtb_reborn > 0 and self.vtb_price >= 114514:
            return '赢'
        else:
            return '输'
    vtb_fire.short_description = '爆火'


# 定义信息类 Ski_info_A
class Ski_info_A(models.Model):
    # 类的属性（表的字段）
    ski_name = models.CharField(max_length=114, default='王牛奶拳', verbose_name='Vtb名称')
    ski_cost = models.FloatField(default=5.14, verbose_name='消耗')
    ski_damage = models.FloatField(default=19.19, verbose_name='伤害')
    ski_cold = models.FloatField(default=2.4, verbose_name='冷却')
    ski_last = models.FloatField(default=0.02, verbose_name='持续')

    # 设置外键属性
    Vtb_info = models.ForeignKey(Vtb_info, on_delete=models.CASCADE, db_column='Vtb_info',
                                 verbose_name='Ski名称')

    # 元属性
    class Meta:
        db_table = 'ski_info'  # 指定数据库中的表的名称 非中文
        verbose_name = 'Ski名称'  # 指定表的别名 可以为中文
        verbose_name_plural = verbose_name  # 指定复数形式也为别名

    def __str__(self):
        return self.ski_name  # 一般返回名称

    # 利用外键得到 vtb 信息
    def show_vtb_name(self):
        return self.Vtb_info.vtb_name
    show_vtb_name.short_description = '装备者'