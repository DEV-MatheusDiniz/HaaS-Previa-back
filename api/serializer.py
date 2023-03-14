from rest_framework import serializers

from .models import Faturamento
from .models import FaturamentoItem
from .models import ItemConfiguracao
from .models import FaturamentoItemConteudo


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


# Faturamento Item Conteudo
class FaturamentoItemConteudoSerializer(serializers.ModelSerializer):

    class Meta:
        model = FaturamentoItemConteudo
        fields = '__all__'
