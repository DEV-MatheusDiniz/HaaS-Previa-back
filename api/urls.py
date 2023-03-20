from django.urls import path, include

from . import views


# Rotas
urlpatterns = [

    # Api Auth
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Faturamentos ALL
    path('faturamentos/', views.FaturamentosAPIView.as_view(), name='faturamentos'),

    # Faturamentos ONE
    path('faturamentos/one/<int:idPrevia>', views.FaturamentosOneAPIView.as_view(), name='faturamentos'),

    # Faturamentos Item ALL
    path('faturamentosItem/<int:idPrevia>', views.FaturamentosItemAPIView.as_view(), name='faturamentosItem'),

    # Faturamentos Item ONE
    path('faturamentosItem/one/<int:idItem>', views.FaturamentosItemOneAPIView.as_view(), name='faturamentoItem'),

    # Item Configuração ALL
    path('itemConfiguracao/', views.ItemConfiguracaoAPIView.as_view(), name='itemConfiguracao'),

    # Faturamento Item Conteudo ALL
    path('faturamentoItemConteudo/<int:id>', views.FaturamentoItemConteudoAPIView.as_view(), name='faturamentoItemConteudo'),

]
