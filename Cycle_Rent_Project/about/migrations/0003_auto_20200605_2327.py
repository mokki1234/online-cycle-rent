# Generated by Django 3.0.7 on 2020-06-05 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='ceobanner',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='header',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='team',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
