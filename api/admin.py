from django.contrib import admin
from .models import Category, Product, ProductImage, Collection, KeyFeature, InstagramPhoto


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
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'category', 'dimensions', 'capacity', 'material', 'weight', 'made_in', 'created_at', 'updated_at')
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
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('products',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(InstagramPhoto, InstagramPhotoAdmin)
