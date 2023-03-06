from django.shortcuts import render
from rest_framework import viewsets

from .models import Faturamento
from .serializer import FaturamentoSerializer


class FaturamentoViewSet(viewsets.ModelViewSet):
    queryset = Faturamento.objects.filter(st_situacao = 'previa').order_by('-dt_cadastro')
    serializer_class = FaturamentoSerializer
