# Generated by Django 3.1.1 on 2020-09-13 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_friend_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='ip',
            field=models.CharField(max_length=20),
        ),
    ]