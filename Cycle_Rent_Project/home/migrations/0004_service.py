# Generated by Django 3.0.7 on 2020-06-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200605_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_title', models.CharField(max_length=120)),
                ('first_description', models.TextField()),
                ('second_title', models.CharField(max_length=120)),
                ('second_description', models.TextField()),
                ('third_title', models.CharField(max_length=120)),
                ('third_description', models.TextField()),
            ],
        ),
    ]
