# Generated by Django 2.1.5 on 2019-01-31 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190131_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverprofile',
            name='is_busy',
            field=models.BooleanField(default=False),
        ),
    ]
