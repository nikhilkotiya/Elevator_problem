# Generated by Django 3.2.5 on 2023-03-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevator_app', '0003_auto_20230327_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevator',
            name='current_floor',
            field=models.IntegerField(default=0),
        ),
    ]
