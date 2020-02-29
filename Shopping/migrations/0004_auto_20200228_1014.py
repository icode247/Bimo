# Generated by Django 3.0.3 on 2020-02-28 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0003_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordereditem',
            old_name='items',
            new_name='item',
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=128355),
        ),
    ]
