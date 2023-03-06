from rest_framework import serializers

from .models import Faturamento


class FaturamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faturamento
        fields = '__all__'
