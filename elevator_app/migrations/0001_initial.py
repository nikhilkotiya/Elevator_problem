# Generated by Django 3.2.5 on 2023-03-26 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('max_floor', models.IntegerField()),
                ('min_floor', models.IntegerField(default=0)),
                ('number_of_elevators', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ElevatorRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_floor', models.IntegerField()),
                ('destination_floor', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('current_floor', models.PositiveSmallIntegerField(default=0)),
                ('is_operational', models.BooleanField(default=True)),
                ('is_door_open', models.BooleanField(default=True)),
                ('running_status', models.CharField(choices=[('going_up', 'Going_Up'), ('standing_still', 'Standing_Still'), ('going_down', 'Going_Down')], default='standing_still', max_length=20)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elevator_app.building')),
            ],
        ),
    ]
