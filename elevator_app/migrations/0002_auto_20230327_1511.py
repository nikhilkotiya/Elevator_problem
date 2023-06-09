# Generated by Django 3.2.5 on 2023-03-27 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevator_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elevatorrequest',
            name='source_floor',
        ),
        migrations.AlterField(
            model_name='elevator',
            name='running_status',
            field=models.CharField(choices=[('going_up', 'Going_Up'), ('standing_still', 'Standing_Still'), ('going_down', 'Going_Down'), ('not_working', 'Not_Working')], default='standing_still', max_length=20),
        ),
    ]
