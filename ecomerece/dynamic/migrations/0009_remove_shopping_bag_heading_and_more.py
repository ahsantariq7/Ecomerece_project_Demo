# Generated by Django 4.0.6 on 2022-08-19 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0008_shopping_bag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_bag',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='shopping_bag',
            name='image',
        ),
        migrations.RemoveField(
            model_name='shopping_bag',
            name='price',
        ),
        migrations.CreateModel(
            name='Shopping_Bag_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='media')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dynamic.shopping_bag')),
            ],
        ),
    ]