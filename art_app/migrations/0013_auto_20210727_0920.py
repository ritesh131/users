# Generated by Django 3.0.2 on 2021-07-27 09:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('art_app', '0012_remove_userart_inspired_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userart',
            name='art_images',
            field=models.ManyToManyField(blank=True, to='art_app.ArtImages'),
        ),
        migrations.AlterField(
            model_name='userart',
            name='comment',
            field=models.ManyToManyField(blank=True, related_name='users_comment', to='art_app.ArtComment'),
        ),
        migrations.AlterField(
            model_name='userart',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='users_like', to=settings.AUTH_USER_MODEL),
        ),
    ]