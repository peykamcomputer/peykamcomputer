# Generated by Django 4.0.3 on 2024-06-22 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_delete_dailytasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField(blank=True, default=None, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('category', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='main.category')),
            ],
        ),
    ]
