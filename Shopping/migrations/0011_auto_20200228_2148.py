# Generated by Django 3.0.3 on 2020-02-29 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0010_auto_20200228_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=852845),
        ),
    ]