# Generated by Django 4.0.3 on 2024-06-20 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500)),
                ('email_1', models.CharField(blank=True, max_length=500)),
                ('email_2', models.CharField(blank=True, max_length=500)),
                ('phone_1', models.CharField(blank=True, max_length=500)),
                ('phone_2', models.CharField(blank=True, max_length=500)),
                ('address_1', models.CharField(blank=True, max_length=500)),
                ('address_2', models.CharField(blank=True, max_length=500)),
                ('work_hours', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Info',
            },
        ),
    ]
