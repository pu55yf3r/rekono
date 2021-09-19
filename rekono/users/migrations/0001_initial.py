# Generated by Django 3.2.7 on 2021-09-19 11:03

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
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_preference', models.IntegerField(blank=True, choices=[(1, 'Mail'), (2, 'Telegram')], default=1, null=True)),
                ('telegram_token', models.TextField(blank=True, max_length=100, null=True)),
                ('binaryedge_apikey', models.TextField(blank=True, max_length=100, null=True)),
                ('bing_apikey', models.TextField(blank=True, max_length=100, null=True)),
                ('censys_apikey', models.TextField(blank=True, max_length=100, null=True)),
                ('github_apikey', models.TextField(blank=True, max_length=100, null=True)),
                ('hunter_apikey', models.TextField(blank=True, max_length=100, null=True)),
                ('intelx_apikey', models.TextField(blank=True, max_length=100, null=True)),
                ('pentestTools_apikey', models.TextField(blank=True, max_length=100, null=True)),
                ('rocketreach_apikey', models.TextField(blank=True, max_length=100, null=True)),
                ('securityTrails_apikey', models.TextField(blank=True, max_length=100, null=True)),
                ('shodan_apikey', models.TextField(blank=True, max_length=100, null=True)),
                ('spyse_apikey', models.TextField(blank=True, max_length=100, null=True)),
                ('zoomeye_apikey', models.TextField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
