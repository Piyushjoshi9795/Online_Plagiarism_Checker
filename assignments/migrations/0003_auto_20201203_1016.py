# Generated by Django 3.1.3 on 2020-12-03 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_auto_20201203_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giveassignment',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
