# Generated by Django 2.0.4 on 2018-05-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_base_rate_average'),
    ]

    operations = [
        migrations.AddField(
            model_name='base',
            name='visibility_flag',
            field=models.BooleanField(db_index=True, default=True, help_text='Boolean'),
        ),
    ]
