# Generated by Django 3.0.3 on 2020-02-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0016_auto_20200229_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordereditem',
            name='seize',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=453850),
        ),
    ]