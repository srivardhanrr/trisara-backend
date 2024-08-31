from rest_framework import viewsets
from .models import Category, Product, Collection, CookbookCategory, Cookbook
from .serializers import CategorySerializer, ProductSerializer, CollectionSerializer, CookbookCategorySerializer, \
    CookbookSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class CollectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = 'slug'


class CookbookCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CookbookCategory.objects.all()
    serializer_class = CookbookCategorySerializer
    lookup_field = 'slug'


class CookbookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cookbook.objects.all()
    serializer_class = CookbookSerializer
    lookup_field = 'slug'
