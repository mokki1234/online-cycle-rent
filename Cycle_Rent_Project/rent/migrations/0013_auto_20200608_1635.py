# Generated by Django 3.0.7 on 2020-06-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0012_auto_20200608_1420'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DestinitionSelect',
        ),
        migrations.AddField(
            model_name='bike',
            name='price',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
