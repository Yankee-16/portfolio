# Generated by Django 3.0.3 on 2020-06-06 14:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 6, 14, 43, 45, 446789, tzinfo=utc)),
        ),
    ]