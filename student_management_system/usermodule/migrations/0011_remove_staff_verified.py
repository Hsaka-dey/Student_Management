# Generated by Django 4.2.5 on 2024-05-21 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0010_approvestudent_approvestaff_approvehod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='verified',
        ),
    ]
