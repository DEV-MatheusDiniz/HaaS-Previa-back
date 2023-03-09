from django.urls import path, include
from rest_framework import routers

from . import views


# Rotas
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('faturamentos/', views.FaturamentoAPIView.as_view(), name='faturamntos'),
    path('faturamentosItem/', views.FaturamentoItemAPIView.as_view(), name='faturamentosItem'),
]
