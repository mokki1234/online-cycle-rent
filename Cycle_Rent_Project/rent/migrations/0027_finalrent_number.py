# Generated by Django 3.0.7 on 2020-06-10 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0026_auto_20200610_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalrent',
            name='number',
            field=models.CharField(default='sjk', max_length=120),
            preserve_default=False,
        ),
    ]
