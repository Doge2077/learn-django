from rest_framework import serializers  # 导入序列化器包

import App_07.models
from App_07.models import Vtb_info  # 导入 vtb 模型类
from App_07.models import Ski_info_A  # 导入 Ski_info_A 模型类


# vtb 信息序列化器的定义
# class vtb_info_serializers(serializers.ModelSerializer):
#     class Meta:
#         model = Vtb_info
#         fields = '__all__'

# 定义 Vtb_info 序列化器类
class vtb_info_serializers(serializers.ModelSerializer):
    # 指定序列化器中的字段属性，进行验证

    vtb_name = serializers.CharField(label='名称', max_length=114)
    vtb_price = serializers.FloatField(label='价格')
    vtb_exp = serializers.IntegerField(label='次数')
    vtb_reborn = serializers.IntegerField(label='转生次数')
    vtb_age = serializers.DateField(label='时间')  # 序列化器里面不做时间的指定
    vtb_image = serializers.ImageField(label='头像', required=False)  # 允许为空值

    # 关联外键
    Ski_info_A_set = serializers.PrimaryKeyRelatedField(read_only=True)

    # 设置元属性
    class Meta:
        model = Vtb_info  # 指定对象的模型类
        fields = '__all__'  # 指定对应字段是否进行序列操作，__all__ 代表将所有字段进行序列化


# 定义 Ski_info_A 的序列化器类
class ski_info_A_serializers(serializers.ModelSerializer):
    # 指定序列化字段属性
    ski_name = serializers.CharField(max_length=114, label='Vtb名称')
    ski_cost = serializers.FloatField(label='消耗')
    ski_damage = serializers.FloatField(label='伤害')
    ski_cold = serializers.FloatField(label='冷却')
    ski_last = serializers.FloatField(label='持续')

    # 关联主键 id
    # Vtb_info = serializers.PrimaryKeyRelatedField(label='所属 vtb', read_only=True)
    # 关联主键信息
    # Vtb_info = serializers.StringRelatedField(label='vtb_name')
    # 序列化主键信息
    Vtb_info = vtb_info_serializers()

    class Meta:
        model = Ski_info_A
        fields = '__all__'
