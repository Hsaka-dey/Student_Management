# Generated by Django 4.2.5 on 2024-04-10 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0003_remove_staff_course_id_staff_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='hod',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='hod',
            name='email_varified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hod',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]