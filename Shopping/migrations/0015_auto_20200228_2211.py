# Generated by Django 3.0.3 on 2020-02-29 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Shopping', '0014_auto_20200228_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='Shopping.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ordereditem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shopping.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=339795),
        ),
    ]
