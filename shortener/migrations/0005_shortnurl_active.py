# Generated by Django 2.2.3 on 2019-07-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20190724_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortnurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
