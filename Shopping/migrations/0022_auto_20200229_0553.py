# Generated by Django 3.0.3 on 2020-02-29 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0021_auto_20200229_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='Shopping.OrderedItem'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=880191),
        ),
    ]
