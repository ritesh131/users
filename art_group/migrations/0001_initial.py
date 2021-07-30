# Generated by Django 3.0.2 on 2021-04-06 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('categoy', models.CharField(choices=[('sport', 'SPORT'), ('education', 'EDUCATION'), ('organization', 'ORGANIZATION'), ('entertainment', 'ENTERTAINMENT')], default='sport', max_length=100)),
                ('about', models.TextField(blank=True, null=True)),
                ('created_on', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]