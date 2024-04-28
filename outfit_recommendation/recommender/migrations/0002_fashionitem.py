# Generated by Django 5.0.3 on 2024-04-28 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FashionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productDisplayName', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('subCategory', models.CharField(max_length=255)),
                ('baseColour', models.CharField(max_length=255)),
                ('articleType', models.CharField(max_length=255)),
                ('masterCategory', models.CharField(max_length=255)),
                ('usage', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
            ],
        ),
    ]
