# Generated by Django 3.0.3 on 2020-03-09 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0043_auto_20200308_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='Phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=787211),
        ),
    ]
