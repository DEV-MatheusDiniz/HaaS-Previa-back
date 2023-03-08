from django.shortcuts import render
from rest_framework import viewsets

from .models import Faturamento, FaturamentoItem
from .serializer import FaturamentoSerializer, FaturamentoItemSerializer


class FaturamentoViewSet(viewsets.ModelViewSet):
    queryset = Faturamento.objects.filter(st_situacao = 'previa').order_by('-dt_cadastro')
    serializer_class = FaturamentoSerializer

class FaturamentoItemViewSet(viewsets.ModelViewSet):
    queryset = FaturamentoItem.objects.filter().order_by('-id')
    serializer_class = FaturamentoItemSerializer
