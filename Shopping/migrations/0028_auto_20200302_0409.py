# Generated by Django 3.0.3 on 2020-03-02 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0027_auto_20200302_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=645426),
        ),
    ]
