# Generated by Django 3.0.7 on 2020-06-10 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0024_finalrent_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalrent',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]