# Generated by Django 5.1 on 2024-09-12 19:58

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Content'),
        ),
    ]
