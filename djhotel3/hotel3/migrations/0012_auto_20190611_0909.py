# Generated by Django 2.2 on 2019-06-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel3', '0011_auto_20190611_0907'),
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
    ]