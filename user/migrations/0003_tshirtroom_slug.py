# Generated by Django 3.1.1 on 2020-09-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200912_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='tshirtroom',
            name='slug',
            field=models.SlugField(default=None, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
