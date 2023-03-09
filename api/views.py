from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Faturamento
from .models import FaturamentoItem
from .models import ItemConfiguracao

from .serializer import FaturamentoSerializer
from .serializer import FaturamentoItemSerializer
from .serializer import ItemConfiguracaoSerializer


# Faturamento
class FaturamentoAPIView(APIView):

    def get(self, request):
        
        faturamentos = Faturamento.objects.filter(st_situacao = 'previa').order_by('-dt_cadastro')
        serializer = FaturamentoSerializer(faturamentos, many=True)

        return Response(serializer.data)


# FaturamentoItem
class FaturamentoItemAPIView(APIView):

    def get(self, reequest, id):

        faturamentoItem = FaturamentoItem.objects.filter(faturamento = id).order_by('-id')

        serializer = FaturamentoItemSerializer(faturamentoItem, many=True)


        for faturamento in faturamentoItem:

            for item in serializer.data:

                for index in item:

                    if index == 'item_configuracao':

                        item['item_configuracao'] = faturamento.item_configuracao.no_item

        return Response(serializer.data)


# Item Configuração
class ItemConfiguracaoAPIView(APIView):

    def get(self, request):

        itemConfiguracao = ItemConfiguracao.objects.all()
        serializer = ItemConfiguracaoSerializer(itemConfiguracao, many=True)

        return Response(serializer.data)
