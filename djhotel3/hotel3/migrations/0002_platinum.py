# Generated by Django 2.2 on 2019-06-10 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platinum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Check_In', models.IntegerField()),
                ('Check_Out', models.IntegerField()),
                ('Room_number', models.IntegerField()),
                ('Room_id', models.IntegerField()),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hotel3.Register')),
            ],
        ),
    ]
