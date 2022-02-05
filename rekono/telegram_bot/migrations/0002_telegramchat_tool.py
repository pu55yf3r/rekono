# Generated by Django 3.2.12 on 2022-02-05 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('telegram_bot', '0001_initial'),
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramchat',
            name='tool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.tool'),
        ),
    ]
