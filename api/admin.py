from django.contrib import admin
from .models import Category, Product, ProductImage, Collection, KeyFeature, InstagramPhoto, CookbookCategory, Cookbook, \
    Ingredient, PreparationStep


class InstagramPhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at', 'updated_at')
    search_fields = ('description',)
    list_filter = ('created_at', 'updated_at')


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class KeyFeatureInline(admin.TabularInline):
    model = KeyFeature
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category', 'dimensions', 'capacity', 'material', 'weight', 'made_in', 'created_at', 'updated_at')
    list_filter = ('category', 'material', 'made_in', 'created_at')
    search_fields = (
        'name', 'description', 'dimensions', 'capacity', 'material', 'weight', 'suitable_heat_sources', 'made_in',
        'key_features')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('Product Details', {
            'fields': ('dimensions', 'capacity', 'material', 'weight', 'suitable_heat_sources', 'made_in')
        }),
    )
    inlines = [ProductImageInline, KeyFeatureInline]


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('products',)


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1


class PreparationStepInline(admin.TabularInline):
    model = PreparationStep
    extra = 1


class CookbookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class CookbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [IngredientInline, PreparationStepInline]
    date_hierarchy = 'created_at'


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('description', 'cookbook')
    list_filter = ('cookbook',)
    search_fields = ('name', 'cookbook__title')


class PreparationStepAdmin(admin.ModelAdmin):
    list_display = ('cookbook', 'step_number', 'description')
    list_filter = ('cookbook',)
    search_fields = ('cookbook__title', 'description')
    ordering = ('cookbook', 'step_number')


# Register models
admin.site.register(CookbookCategory, CookbookCategoryAdmin)
admin.site.register(Cookbook, CookbookAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(PreparationStep, PreparationStepAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(InstagramPhoto, InstagramPhotoAdmin)
