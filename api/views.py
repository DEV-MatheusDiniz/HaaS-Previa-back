from rest_framework.views import APIView
from rest_framework.response import Response

import locale

from datetime import datetime
from dateutil.parser import parse

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

        for item in serializer.data:

            # Regra de Faturamento
            if item['bo_regra_cobranca']:

                item['bo_regra_cobranca'] = 'APLICADA'

            else:

                item['bo_regra_cobranca'] = 'NÃO APLICADA'

            # Dia/Mes de Referencia
            data_referencia = datetime.strptime(item['dt_mes_referencia'], '%Y-%m-%d')

            if item['bo_diario']:

                # dia/mes/ano
                item['dt_mes_referencia'] = data_referencia.strftime('%d/%m/%Y')
            else:

                # Nome do mês
                item['dt_mes_referencia'] = data_referencia.strftime('%B/%Y')

            # Valor Total em US's
            item['vl_total_grupo'] = 'US ' +  locale.currency(float(item["vl_total_grupo"]), grouping=True, symbol=False)

            # Valor Total Mensal
            item['vl_total_mensal'] = locale.currency(float(item['vl_total_mensal']), grouping=True)

            # Data Processada
            item['dt_cadastro'] = "{dia}/{mes}/{ano} - {hora}".format(
                dia=item['dt_cadastro'][8:10],
                mes=item['dt_cadastro'][5:7],
                ano=item['dt_cadastro'][0:4],
                hora=item['dt_cadastro'][11:16])

        return Response(serializer.data)


# FaturamentoItem
class FaturamentoItemAPIView(APIView):

    def get(self, reequest, id):

        faturamentoItem = FaturamentoItem.objects.filter(faturamento = id).order_by('item_configuracao')

        serializer = FaturamentoItemSerializer(faturamentoItem, many=True)


        for item in serializer.data:

                for index in item:

                    if index == 'item_configuracao':

                        for faturamento in faturamentoItem:
                            
                            if faturamento.item_configuracao.id == item[index]:

                                item[index] = faturamento.item_configuracao.no_item

        return Response(serializer.data)


# Item Configuração
class ItemConfiguracaoAPIView(APIView):

    def get(self, request):

        itemConfiguracao = ItemConfiguracao.objects.all()

        serializer = ItemConfiguracaoSerializer(itemConfiguracao, many=True)

        return Response(serializer.data)
