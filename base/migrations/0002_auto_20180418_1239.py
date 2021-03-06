# Generated by Django 2.0.4 on 2018-04-18 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report_related_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_related_user_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rate',
            name='rate_related_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_related_parent_name', to='base.Base'),
        ),
        migrations.AddField(
            model_name='rate',
            name='rate_related_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_related_user_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favorite',
            name='favorite_related_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_related_parent_name', to='base.Base'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='favorite_related_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_related_user_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='discount',
            name='discount_related_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount_related_parent_name', to='base.Base'),
        ),
        migrations.AddField(
            model_name='discount',
            name='discount_related_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount_related_user_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_related_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_related_parent_name', to='base.Base'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_related_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_related_user_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
