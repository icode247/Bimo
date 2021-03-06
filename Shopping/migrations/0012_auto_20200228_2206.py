# Generated by Django 3.0.3 on 2020-02-29 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Shopping', '0011_auto_20200228_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, to='Shopping.product'),
        ),
        migrations.RemoveField(
            model_name='ordereditem',
            name='item',
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shopping.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=955103),
        ),
    ]
