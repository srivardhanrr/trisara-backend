from rest_framework import viewsets
from .models import Category, Product, Collection, CookbookCategory, Cookbook, InstagramPhoto, Series, Blog, HeroImage
from .serializers import CategorySerializer, ProductSerializer, CollectionSerializer, CookbookCategorySerializer, \
    CookbookSerializer, InstagramPhotoSerializer, SeriesSerializer, BlogSerializer, HeroImageSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class HeroImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HeroImage.objects.all()
    serializer_class = HeroImageSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class SeriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    lookup_field = 'slug'


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'category__name', 'series__name']
    filterset_fields = ['category', 'series', 'new_badge', 'best_seller']


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


class InstagramPostsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InstagramPhoto.objects.all()
    serializer_class = InstagramPhotoSerializer


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    lookup_field = 'slug'
