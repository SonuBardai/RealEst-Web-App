# Generated by Django 3.2.9 on 2022-03-12 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0015_properties_image_compressed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='image_compressed',
        ),
    ]
