# Generated by Django 3.0.3 on 2020-03-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0025_auto_20200302_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=201967),
        ),
    ]
