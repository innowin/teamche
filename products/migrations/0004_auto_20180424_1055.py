# Generated by Django 2.0.4 on 2018-04-24 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180424_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_related_brand',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]