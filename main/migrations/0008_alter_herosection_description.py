# Generated by Django 4.0.3 on 2024-06-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_herosection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herosection',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
