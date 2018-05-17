# Generated by Django 2.0.4 on 2018-05-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0006_store_related_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='active_flag',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.CharField(blank=True, db_index=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='latitude',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=10, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='longitude',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=10, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone_number',
            field=models.CharField(blank=True, db_index=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='storecategory',
            name='title',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='storevisit',
            name='active_flag',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
