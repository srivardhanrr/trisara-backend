# Generated by Django 5.1 on 2024-08-30 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_cookbook_slug_cookbookcategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookbook',
            name='image',
            field=models.ImageField(blank=True, upload_to='cookbooks/'),
        ),
    ]
