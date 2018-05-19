# Generated by Django 2.0.4 on 2018-05-17 09:35

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_base_visibility_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='rate_average',
            field=models.DecimalField(db_index=True, decimal_places=2, default=Decimal('0.00'), max_digits=5),
        ),
        migrations.AlterField(
            model_name='comment',
            name='active_flag',
            field=models.BooleanField(db_index=True, default=True),
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount_value',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='value',
            field=models.DecimalField(db_index=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='slider',
            name='link',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sms',
            name='code',
            field=models.CharField(db_index=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='sms',
            name='phone_number',
            field=models.CharField(db_index=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='topfilter',
            name='link',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='topfilter',
            name='order',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='topfilter',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
    ]