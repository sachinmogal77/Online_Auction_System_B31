# Generated by Django 4.1.3 on 2022-11-21 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('response', models.TextField()),
                ('feedback_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
