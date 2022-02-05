# Generated by Django 3.2.12 on 2022-02-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(choices=[('OSINT', 'Osint'), ('Host', 'Host'), ('Enumeration', 'Enumeration'), ('Endpoint', 'Endpoint'), ('Technology', 'Technology'), ('Vulnerability', 'Vulnerability'), ('Exploit', 'Exploit'), ('Credential', 'Credential'), ('Wordlist', 'Wordlist')], max_length=15)),
                ('related_model', models.TextField(max_length=30)),
                ('callback_target', models.TextField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
