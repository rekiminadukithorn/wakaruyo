# Generated by Django 2.1.15 on 2020-05-26 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20200525_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='is_done',
        ),
    ]
