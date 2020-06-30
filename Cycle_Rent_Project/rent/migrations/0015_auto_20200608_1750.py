# Generated by Django 3.0.7 on 2020-06-08 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rent', '0014_bookedtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectet_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.SelectPoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='BookedTime',
        ),
    ]
