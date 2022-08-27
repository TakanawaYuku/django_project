from rest_framework.viewsets import ModelViewSet
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
#здесь делал по уроку и тот путь который указан в уроке у меня почему то не работал и он его не видел, пришлось как то выкручиваться и вроде при таком случае он видит путь
# from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import DjangoFilterBackend


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = [
        'id',
        'title',
        'description',
    ]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all().prefetch_related('positions')
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = [
        'products',
    ]
    search_fields = ['products__title', 'products__description']
