# Generated by Django 2.1.15 on 2020-05-09 18:22

# Generated by Django 2.1.15 on 2020-05-10 07:41

# Generated by Django 2.1.15 on 2020-05-10 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.CharField(blank=True, max_length=50, verbose_name='Twitter'),
        ),
    ]
