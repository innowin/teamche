# Generated by Django 2.0.4 on 2018-04-18 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Base')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True)),
            ],
            bases=('base.base',),
        ),
        migrations.CreateModel(
            name='StoreCategory',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Base')),
                ('title', models.CharField(max_length=50)),
            ],
            bases=('base.base',),
        ),
        migrations.CreateModel(
            name='StoreVisit',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Base')),
                ('store_visit_related_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_visit_related_store', to='stores.Store')),
            ],
            bases=('base.base',),
        ),
    ]
