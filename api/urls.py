from django.urls import path, include

from . import views


# Rotas
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('faturamentos/', views.FaturamentoAPIView.as_view(), name='faturamntos'),
    path('faturamentosItem/<int:id>', views.FaturamentoItemAPIView.as_view(), name='faturamentosItem'),
    path('itemConfiguracao/', views.ItemConfiguracaoAPIView.as_view(), name='itemConfiguracao'),
]
