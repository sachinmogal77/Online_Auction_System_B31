# Generated by Django 4.1.3 on 2022-11-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, upload_to='product_images/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInformation',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=30)),
                ('product_description', models.TextField()),
                ('product_manufacture_year', models.PositiveIntegerField()),
                ('product_base_price', models.FloatField()),
                ('product_verify', models.BooleanField(default=False)),
            ],
        ),
    ]
