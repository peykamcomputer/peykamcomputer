# Generated by Django 4.0.3 on 2024-07-03 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_aboutus_full_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploadInstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('description', models.TextField(blank=True)),
                ('title_russian', models.CharField(blank=True, max_length=250)),
                ('description_russian', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'File Upload Instruction',
                'verbose_name_plural': 'File Upload Instructions',
            },
        ),
    ]
