# Generated by Django 4.2.7 on 2024-02-04 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_coverimage_suzdaluser_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suzdaluser',
            name='price',
        ),
    ]