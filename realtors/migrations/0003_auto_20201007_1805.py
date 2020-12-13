# Generated by Django 3.1.2 on 2020-10-08 01:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20201006_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='phone',
            field=models.CharField(default='03000000', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 7, 18, 4, 16, 474026)),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(upload_to='photo/%Y/%m/%d/'),
        ),
    ]
