# Generated by Django 3.0.3 on 2020-03-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0024_auto_20200302_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=151620),
        ),
    ]