# Generated by Django 3.0.6 on 2020-06-04 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20200604_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='logo',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
    ]