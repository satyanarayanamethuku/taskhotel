# Generated by Django 2.2 on 2019-06-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel3', '0002_platinum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platinum',
            name='Check_In',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='platinum',
            name='Check_Out',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='platinum',
            name='Room_number',
            field=models.CharField(choices=[('1', '101'), ('2', '102'), ('3', '103'), ('4', '104'), ('5', '105')], max_length=64),
        ),
    ]
