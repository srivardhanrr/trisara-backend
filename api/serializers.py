from rest_framework import serializers
from .models import Category, Product, ProductImage, Collection, KeyFeature, InstagramPhoto, CookbookCategory, Cookbook, \
    Ingredient, PreparationStep


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





class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'description']


class PreparationStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreparationStep
        fields = ['id', 'step_number', 'description']


class CookbookSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    preparation_steps = PreparationStepSerializer(many=True, read_only=True)

    class Meta:
        model = Cookbook
        fields = ['id', 'title', 'image', 'slug', 'description', 'created_at', 'updated_at', 'ingredients',
                  'preparation_steps']


class CookbookCategorySerializer(serializers.ModelSerializer):
    cookbooks = CookbookSerializer(many=True, read_only=True)

    class Meta:
        model = CookbookCategory
        fields = ['id', 'name', 'cookbooks', 'slug', 'image']
