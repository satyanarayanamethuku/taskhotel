# Generated by Django 2.2 on 2019-06-11 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel3', '0006_auto_20190611_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='platinum',
            name='Room_id',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
