from rest_framework import serializers

from .models import Faturamento
from .models import FaturamentoItem
from .models import ItemConfiguracao


# Faturamento
class FaturamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faturamento
        fields = '__all__'


# Faturamento Item
class FaturamentoItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FaturamentoItem
        fields = '__all__'


# Item de Configuração
class ItemConfiguracaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemConfiguracao
        fields = '__all__'
