# Generated by Django 3.1 on 2020-10-04 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200913_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
