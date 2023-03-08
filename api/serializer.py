from rest_framework import serializers

from .models import Faturamento, FaturamentoItem


class FaturamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faturamento
        fields = '__all__'

class FaturamentoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaturamentoItem
        fields = '__all__'
