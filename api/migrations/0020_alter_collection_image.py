# Generated by Django 5.1 on 2024-09-18 18:52

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_category_image_alter_collection_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[1080, 1080], upload_to='categories/'),
        ),
    ]