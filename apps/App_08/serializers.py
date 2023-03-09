from rest_framework import serializers  # 导入序列化器包
from App_07.models import Vtb_info  # 导入 vtb 模型类


# vtb 信息序列化器的定义
class vtb_info_serializers(serializers.ModelSerializer):
    class Meta:
        model = Vtb_info
        fields = '__all__'
