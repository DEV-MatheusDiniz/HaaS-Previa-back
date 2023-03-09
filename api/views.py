from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Faturamento, FaturamentoItem
from .serializer import FaturamentoSerializer, FaturamentoItemSerializer


# Faturamento
class FaturamentoAPIView(APIView):

    def get(self, request):
        faturamentos = Faturamento.objects.filter(st_situacao = 'previa').order_by('-dt_cadastro')
        serializer = FaturamentoSerializer(faturamentos, many=True)
        return Response(serializer.data)


# FaturamentoItem
class FaturamentoItemAPIView(APIView):

    def get(self, reequest):
        faturamentoItem = FaturamentoItem.objects.all().order_by('-id')
        serializer = FaturamentoItemSerializer(faturamentoItem, many=True)
        return Response(serializer.data)
