# Generated by Django 4.0.4 on 2022-07-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papp', '0005_generatepassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.URLField()),
            ],
        ),
    ]
