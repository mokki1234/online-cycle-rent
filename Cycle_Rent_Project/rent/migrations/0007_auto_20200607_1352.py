# Generated by Django 3.0.7 on 2020-06-07 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0006_auto_20200607_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
