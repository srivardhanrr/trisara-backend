# Generated by Django 5.1 on 2024-09-18 18:57

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_collection_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[1080, 1080], upload_to='blogs/'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[1080, 1080], upload_to='collections/'),
        ),
        migrations.AlterField(
            model_name='cookbook',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[1080, 1080], upload_to='cookbooks/'),
        ),
        migrations.AlterField(
            model_name='cookbookcategory',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[1080, 1080], upload_to='cookbook_categories/'),
        ),
        migrations.AlterField(
            model_name='instagramphoto',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[1080, 1080], upload_to='instagram/'),
        ),
        migrations.AlterField(
            model_name='series',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, quality=90, scale=None, size=[1080, 1080], upload_to='series/'),
        ),
    ]