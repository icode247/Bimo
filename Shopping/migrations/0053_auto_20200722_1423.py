# Generated by Django 3.0.3 on 2020-07-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0052_auto_20200722_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available_item',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=670375),
        ),
    ]
