# Generated by Django 4.0.6 on 2022-08-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_By_Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_logo', models.ImageField(upload_to='')),
            ],
        ),
    ]