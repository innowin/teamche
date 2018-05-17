# Generated by Django 2.0.4 on 2018-05-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_active_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='active_flag',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='made_in_iran',
            field=models.BooleanField(db_index=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='amount',
            field=models.IntegerField(db_index=True),
        ),
    ]
