# Generated by Django 4.0 on 2023-08-15 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_flower_image_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='gardens',
            field=models.ManyToManyField(to='main_app.Garden'),
        ),
    ]
