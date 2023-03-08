from django.urls import path, include
from rest_framework import routers

from .views import FaturamentoViewSet, FaturamentoItemViewSet


# Registro Rotas
router = routers.DefaultRouter()
router.register(r'faturamentos', FaturamentoViewSet)
router.register(r'faturamentosItem', FaturamentoItemViewSet)


# Rotas
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
