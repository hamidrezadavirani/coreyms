# Generated by Django 2.2.7 on 2019-11-20 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191120_0354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titl',
            new_name='title',
        ),
    ]
