# Generated by Django 3.0.3 on 2020-02-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0015_auto_20200228_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=484096),
        ),
    ]
