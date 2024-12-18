from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category, Product, Collection, CookbookCategory, Cookbook, InstagramPhoto, Series, Blog, HeroImage, \
    HomePageSettings
from .serializers import CategorySerializer, ProductSerializer, CollectionSerializer, CookbookCategorySerializer, \
    CookbookSerializer, InstagramPhotoSerializer, SeriesSerializer, BlogSerializer, HeroImageSerializer, \
    HomePageSettingsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


@method_decorator(cache_page(60 * 30), name='dispatch')
class HeroImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HeroImage.objects.all()
    serializer_class = HeroImageSerializer


@method_decorator(cache_page(60 * 30), name='dispatch')
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


@method_decorator(cache_page(60 * 30), name='dispatch')
class SeriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    lookup_field = 'slug'


@method_decorator(cache_page(60 * 30), name='dispatch')
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'category__name', 'series__name']
    filterset_fields = ['category', 'series', 'new_badge', 'best_seller']


@method_decorator(cache_page(60 * 30), name='dispatch')
class CollectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = 'slug'


@method_decorator(cache_page(60 * 30), name='dispatch')
class CookbookCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CookbookCategory.objects.all()
    serializer_class = CookbookCategorySerializer
    lookup_field = 'slug'


@method_decorator(cache_page(60 * 30), name='dispatch')
class CookbookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cookbook.objects.all()
    serializer_class = CookbookSerializer
    lookup_field = 'slug'


@method_decorator(cache_page(60 * 30), name='dispatch')
class InstagramPostsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InstagramPhoto.objects.all()
    serializer_class = InstagramPhotoSerializer


@method_decorator(cache_page(60 * 30), name='dispatch')
class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    lookup_field = 'slug'


@method_decorator(cache_page(60 * 30), name='dispatch')
class HomePageSettingsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomePageSettings.objects.all()
    serializer_class = HomePageSettingsSerializer

    def list(self, request):
        instance = self.get_queryset().first()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
