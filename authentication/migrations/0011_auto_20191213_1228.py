# Generated by Django 2.2.7 on 2019-12-13 12:28

import authentication.models
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20191204_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, default=None, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/media/picture/', location='/opt/apps/media/picture'), upload_to=authentication.models.user_directory_path),
        ),
    ]