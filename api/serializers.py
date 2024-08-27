from rest_framework import serializers
from .models import Category, Product, ProductImage, Collection, KeyFeature, InstagramPhoto


class KeyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyFeature
        fields = ['feature']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    features = KeyFeatureSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description', 'slug', 'dimensions',
                  'capacity', 'material', 'weight', 'suitable_heat_sources',
                  'made_in', 'images', 'features', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'description', 'slug', 'products']


class CollectionSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = ['id', 'name', 'image', 'description', 'slug', 'products']


class InstagramPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramPhoto
        fields = ['id', 'image', 'link', 'description', 'created_at', 'updated_at']
