from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, CollectionViewSet, CookbookCategoryViewSet, CookbookViewSet, \
    InstagramPostsViewSet, SeriesViewSet, BlogViewSet, HeroImageViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'collections', CollectionViewSet)
router.register(r'cookbook-categories', CookbookCategoryViewSet)
router.register(r'cookbooks', CookbookViewSet)
router.register(r'instagram', InstagramPostsViewSet)
router.register(r'series', SeriesViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'hero-images', HeroImageViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
