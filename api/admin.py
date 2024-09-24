from django.contrib import admin
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms

from .models import Category, Product, ProductImage, Collection, KeyFeature, InstagramPhoto, CookbookCategory, Cookbook, \
    Ingredient, PreparationStep, Series, Blog, UsageInstruction, Specification, ProductVariant, HeroImage, \
    ProductInfographic, HomePageSettings


class InstagramPhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at', 'updated_at')
    search_fields = ('description',)
    list_filter = ('created_at', 'updated_at')


class HeroImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


class KeyFeatureInline(admin.TabularInline):
    model = KeyFeature
    extra = 1


class UsageInstructionInline(admin.TabularInline):
    model = UsageInstruction
    extra = 1


class SpecificationInline(admin.TabularInline):
    model = Specification
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}


class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}


class ProductInfographicAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = (
        'name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductVariantInline, KeyFeatureInline, UsageInstructionInline, SpecificationInline]


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


class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(
                config_name='extends',
                attrs={'class': 'django_ckeditor_5'},  # Use the config named 'extends' that we defined in settings.py
            )
        }


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'description', 'content', 'slug')
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('created_at',)
        return self.readonly_fields


class HomePageSettingsAdmin(admin.ModelAdmin):
    list_display = ('collection_1', 'collection_2')

    def has_add_permission(self, request):
        return not HomePageSettings.objects.exists()


admin.site.register(CookbookCategory, CookbookCategoryAdmin)
admin.site.register(Cookbook, CookbookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(InstagramPhoto, InstagramPhotoAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(HeroImage, HeroImageAdmin)
admin.site.register(ProductInfographic, ProductInfographicAdmin)
admin.site.register(HomePageSettings, HomePageSettingsAdmin)
