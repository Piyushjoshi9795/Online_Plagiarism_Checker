# Generated by Django 3.1.3 on 2020-12-04 09:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0005_auto_20201203_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadassignment',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]