# Generated by Django 3.0.3 on 2020-03-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0031_auto_20200302_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='Time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=961910),
        ),
    ]
