# Generated by Django 2.2 on 2019-06-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel3', '0013_platinum_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platinum',
            name='Room_type',
            field=models.CharField(choices=[('Platinum', 'Platinum'), ('Suit', 'Suit')], max_length=64),
        ),
    ]
