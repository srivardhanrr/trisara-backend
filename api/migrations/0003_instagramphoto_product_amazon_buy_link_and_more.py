# Generated by Django 5.1 on 2024-08-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_product_key_features_keyfeature'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='instagram/')),
                ('link', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='amazon_buy_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='blinkIt_buy_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='flipkart_buy_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='zepto_buy_link',
            field=models.URLField(blank=True),
        ),
    ]
