from rest_framework import serializers
from .models import Category, Product, ProductImage, Collection, KeyFeature, InstagramPhoto, CookbookCategory, Cookbook, \
    Ingredient, PreparationStep, Series, Blog, UsageInstruction, Specification, ProductVariant, HeroImage


class HeroImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroImage
        fields = ['image', 'title', 'created_at', 'updated_at']


class KeyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyFeature
        fields = ['feature']


class UsageInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageInstruction
        fields = ['instruction']


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ['label', 'value']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    features = KeyFeatureSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    instructions = UsageInstructionSerializer(many=True, read_only=True)
    specifications = SpecificationSerializer(many=True, read_only=True)
    variants = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'description', 'slug', 'products']


class SeriesSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Series
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


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'description', 'content', 'created_at', 'updated_at', 'slug']
