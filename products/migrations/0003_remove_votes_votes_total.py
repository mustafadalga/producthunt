# Generated by Django 2.2.4 on 2019-08-25 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190825_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='votes_total',
        ),
    ]
