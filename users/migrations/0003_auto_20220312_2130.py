# Generated by Django 3.2.9 on 2022-03-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]