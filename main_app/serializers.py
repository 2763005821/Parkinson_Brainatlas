#这一步告诉 Django 如何将模型变成 JSON（让前端能用）
from rest_framework import serializers
from .models import cell_atlas

class CellAtlasSerializer(serializers.ModelSerializer):
    class Meta:
        model = cell_atlas
        fields = '__all__'
