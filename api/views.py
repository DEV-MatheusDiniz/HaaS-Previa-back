from rest_framework.views import APIView
from rest_framework.response import Response

import locale
from datetime import datetime
from typing import Optional

from .models import Faturamento
from .models import FaturamentoItem
from .models import ItemConfiguracao
from .models import FaturamentoItemConteudo

from .serializer import FaturamentoSerializer
from .serializer import FaturamentoItemSerializer
from .serializer import ItemConfiguracaoSerializer
from .serializer import FaturamentoItemConteudoSerializer


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


# Faturamentos Items
class FaturamentosItemAPIView(APIView):

    def get(self, request, idPrevia):

        faturamentosItem = FaturamentoItem.objects.filter(faturamento = idPrevia).order_by('item_configuracao')

        serializer = FaturamentoItemSerializer(faturamentosItem, many=True)


        for item in serializer.data:

            # Descrição
            itemConfiguracao = ItemConfiguracao.objects.filter(id = item['item_configuracao'])
            
            for ic in itemConfiguracao:

                item['item_configuracao'] = ic.no_item

            # % Relevância
            item['vl_relevancia'] = item['vl_relevancia'] + '%'

            # % Diversidade
            item['vl_diversidade'] = item['vl_diversidade'] + '%'

            # Quantidade de US's estimada para consumo unitario
            item['vl_item'] = locale.currency(float(item['vl_item']), symbol=False, grouping=True)

            # Quantidade de US's estimada para consumo por grupo
            item['vl_total_item'] = locale.currency(float(item['vl_total_item']), symbol=False, grouping=True)

            # Valor mensal para a sustenção do item
            item['vl_total_faturado'] = locale.currency(float(item['vl_total_faturado']), symbol=False, grouping=True)

        return Response(serializer.data)
    

# Faturamento Item
class FaturamentoItemAPIView(APIView):

    def get (self, request, idItem):

        faturamentoItem = FaturamentoItem.objects.filter(id = idItem)

        serializer = FaturamentoItemSerializer(faturamentoItem, many=True)

        for item in serializer.data:

            # Descrição
            itemConfiguracao = ItemConfiguracao.objects.filter(id = item['item_configuracao'])
            
            for ic in itemConfiguracao:

                item['item_configuracao'] = ic.no_item

            # % Relevância
            item['vl_relevancia'] = item['vl_relevancia'] + '%'

            # % Diversidade
            item['vl_diversidade'] = item['vl_diversidade'] + '%'

            # Quantidade de US's estimada para consumo unitario
            item['vl_item'] = locale.currency(float(item['vl_item']), symbol=False, grouping=True)

            # Quantidade de US's estimada para consumo por grupo
            item['vl_total_item'] = locale.currency(float(item['vl_total_item']), symbol=False, grouping=True)

            # Valor mensal para a sustenção do item
            item['vl_total_faturado'] = locale.currency(float(item['vl_total_faturado']), symbol=False, grouping=True)

        return Response(serializer.data) 


# Faturamento Item Conteudo
class FaturamentoItemConteudoAPIView(APIView):
    
    def get(self, request, id):

        faturamentoItemConteudo = FaturamentoItemConteudo.objects.filter(faturamento_item = id)

        serializer = FaturamentoItemConteudoSerializer(faturamentoItemConteudo, many=True)

        return Response(serializer.data)


# Item Configuração
class ItemConfiguracaoAPIView(APIView):

    def get(self, request):

        itemConfiguracao = ItemConfiguracao.objects.all()

        serializer = ItemConfiguracaoSerializer(itemConfiguracao, many=True)

        return Response(serializer.data)
