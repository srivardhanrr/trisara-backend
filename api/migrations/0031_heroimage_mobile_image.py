# Generated by Django 5.1.2 on 2024-11-17 18:23

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_keyfeature_description_usageinstruction_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroimage',
            name='mobile_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, quality=90, scale=None, size=[1920, 1080], upload_to='hero/'),
        ),
    ]