# Generated by Django 2.2.7 on 2019-11-21 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='porfile',
            name='test',
            field=models.CharField(default='', max_length=20),
        ),
    ]
