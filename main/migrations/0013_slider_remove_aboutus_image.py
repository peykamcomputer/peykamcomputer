# Generated by Django 4.0.3 on 2024-06-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='image',
        ),
    ]
