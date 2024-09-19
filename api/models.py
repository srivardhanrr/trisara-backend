from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')
    image = ResizedImageField(size=[1000, 1000], upload_to='categories/', blank=True,
                              force_format='WEBP', quality=75, crop=['middle', 'center'])
    description = models.TextField(blank=True)
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
    image = ResizedImageField(size=[1080, 1080], upload_to='series/', blank=True,
                                      force_format='WEBP', quality=90)
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
    set = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.SET_NULL, null=True)
    series = models.ForeignKey('Series', related_name='products', on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    buy_link = models.URLField(max_length=200, blank=True)
    new_badge = models.BooleanField(default=False)
    best_seller = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)
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


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    variant = models.CharField(max_length=200)
    image = ResizedImageField(size=[1000, 1000], upload_to='products/variants/', blank=True,
                              force_format='WEBP', quality=90)

    def __str__(self):
        return self.variant


class Specification(models.Model):
    product = models.ForeignKey(Product, related_name='specifications', on_delete=models.CASCADE)
    label = models.CharField(max_length=100, blank=True)
    value = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.label


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = ResizedImageField(size=[1000, 1000], upload_to='products/', blank=True,
                              force_format='WEBP', quality=90)


class KeyFeature(models.Model):
    product = models.ForeignKey(Product, related_name='features', on_delete=models.CASCADE)
    feature = models.CharField(max_length=200)

    def __str__(self):
        return self.feature


class UsageInstruction(models.Model):
    product = models.ForeignKey(Product, related_name='instructions', on_delete=models.CASCADE)
    instruction = models.CharField(max_length=200)

    def __str__(self):
        return self.instruction


class Collection(models.Model):
    name = models.CharField(max_length=100)
    image = ResizedImageField(size=[1080, 1080], upload_to='collections/', blank=True,
                              force_format='WEBP', quality=75, crop=['middle', 'center'])
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
    image = ResizedImageField(size=[1080, 1080], upload_to='instagram/', blank=True,
                              force_format='WEBP', quality=75)
    link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description[:50]


class CookbookCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    image = ResizedImageField(size=[1080, 1080], upload_to='cookbook_categories/', blank=True,
                              force_format='WEBP', quality=75, crop=['middle', 'center'])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Cookbook(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = ResizedImageField(size=[1080, 1080], upload_to='cookbooks/', blank=True,
                              force_format='WEBP', quality=75)
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
    image = ResizedImageField(size=[1080, 1080], upload_to='blogs/', blank=True,
                              force_format='WEBP', quality=75)
    description = models.TextField(blank=True)
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
