from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='series/')
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.SET_NULL, null=True)
    series = models.ForeignKey('Series', related_name='products', on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    amazon_buy_link = models.URLField(max_length=200, blank=True)
    flipkart_buy_link = models.URLField(max_length=200, blank=True)
    zepto_buy_link = models.URLField(max_length=200, blank=True)
    blinkIt_buy_link = models.URLField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    material = models.CharField(max_length=100, blank=True)
    diameter = models.CharField(max_length=50, blank=True)
    weight = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=50, blank=True)
    handle = models.CharField(max_length=100, blank=True)
    pre_seasoned = models.CharField(max_length=10, blank=True)
    dishwasher_safe = models.CharField(max_length=10, blank=True)
    cooktop_compatibility = models.CharField(max_length=100, blank=True)
    sizes_included = models.CharField(max_length=100, blank=True)
    bowl_diameter = models.CharField(max_length=50, blank=True)
    glass_capacity = models.CharField(max_length=50, blank=True)
    snack_rice_plate_diameter = models.CharField(max_length=50, blank=True)
    dinner_plate_diameter = models.CharField(max_length=50, blank=True)
    spoon_length = models.CharField(max_length=50, blank=True)
    size_included = models.CharField(max_length=50, blank=True)
    number_of_plates = models.CharField(max_length=20, blank=True)
    idli_per_plate = models.CharField(max_length=20, blank=True)
    made_in = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')


class KeyFeature(models.Model):
    product = models.ForeignKey(Product, related_name='features', on_delete=models.CASCADE)
    feature = models.CharField(max_length=200)

    def __str__(self):
        return self.feature


class Collection(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='collections/')
    description = models.TextField()
    products = models.ManyToManyField(Product, related_name='collections')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class InstagramPhoto(models.Model):
    image = models.ImageField(upload_to='instagram/')
    link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description[:50]


class CookbookCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='cookbook_categories/', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Cookbook(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='cookbooks/', blank=True)
    category = models.ForeignKey(CookbookCategory, on_delete=models.CASCADE, related_name='cookbooks')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Ingredient(models.Model):
    cookbook = models.ForeignKey(Cookbook, on_delete=models.CASCADE, related_name='ingredients')
    description = models.CharField(max_length=100)


class PreparationStep(models.Model):
    cookbook = models.ForeignKey(Cookbook, on_delete=models.CASCADE, related_name='preparation_steps')
    step_number = models.PositiveIntegerField()
    description = models.TextField()

    class Meta:
        ordering = ['step_number']


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs/', blank=True)
    content = CKEditor5Field('Content', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

