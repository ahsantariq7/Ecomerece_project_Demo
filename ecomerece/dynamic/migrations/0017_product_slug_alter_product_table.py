# Generated by Django 4.0.6 on 2022-08-25 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0016_delete_trending_items_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterModelTable(
            name='product',
            table='app_Product',
        ),
    ]