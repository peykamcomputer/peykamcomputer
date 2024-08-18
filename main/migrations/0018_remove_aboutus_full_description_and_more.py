# Generated by Django 4.0.3 on 2024-07-01 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_aboutus_full_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='full_description',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='full_description_russian',
        ),
        migrations.AddField(
            model_name='herosection',
            name='components',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='herosection',
            name='components_russian',
            field=models.TextField(blank=True),
        ),
    ]
