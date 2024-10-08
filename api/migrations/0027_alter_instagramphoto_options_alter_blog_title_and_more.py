# Generated by Django 5.1 on 2024-09-24 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_instagramphoto_ordering_homepagesettings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instagramphoto',
            options={'ordering': ['ordering']},
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='cookbook',
            name='title',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='heroimage',
            name='link',
            field=models.URLField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='heroimage',
            name='title',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='instagramphoto',
            name='link',
            field=models.URLField(max_length=400),
        ),
        migrations.AlterField(
            model_name='keyfeature',
            name='feature',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='product',
            name='buy_link',
            field=models.URLField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='variant',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='specification',
            name='value',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='usageinstruction',
            name='instruction',
            field=models.CharField(max_length=400),
        ),
    ]
