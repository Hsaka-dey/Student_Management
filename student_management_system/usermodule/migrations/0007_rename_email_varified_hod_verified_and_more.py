# Generated by Django 4.2.5 on 2024-04-20 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0006_staff_approved_by_student_approved_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hod',
            old_name='email_varified',
            new_name='verified',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='email_varified',
            new_name='verified',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='email_varified',
            new_name='verified',
        ),
    ]
