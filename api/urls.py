from django.urls import path, include
from rest_framework import routers

from .views import FaturamentoViewSet


router = routers.DefaultRouter()
router.register(r'faturamentos', FaturamentoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
