# Generated by Django 3.0.3 on 2020-05-28 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituition', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('start', models.CharField(max_length=30)),
                ('present', models.BooleanField(default=False)),
                ('end', models.CharField(max_length=30, null=True)),
                ('result', models.CharField(max_length=30, null=True)),
                ('logo', models.ImageField(upload_to='media/images/')),
            ],
        ),
    ]