# Generated by Django 4.2.5 on 2024-04-08 12:39

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import usermodule.models

SEMESTER_CHOICES = (
    ("1st", '1st Semester'),
    ("2nd", '2nd Semester'),
    ("3rd", '3rd Semester'),
    ("4th", '4th Semester'),
    ("5th", '5th Semester'),
    ("6th", '6th Semester'),
)

YEAR_CHOICES = (
    ("1st", '1st Year'),
    ("1st", '1st Year'),
    ("2nd", '2nd Year'),
    ("2nd", '2nd Year'),
    ("3rd", '3rd Year'),
    ("3rd", '3rd Year'),
)

DEPT_CHOICES = (
    ("CST", "Computer Science and Technology"),
    ("EE", "Electrical Engineering"),
    ("ME", "Mechanical Engineering"),
    ("ETC", "Electronics and Telecommunication Engineering"),
)

def initialize_semesters(apps, schema_editor):
    Semester = apps.get_model('usermodule', 'Semester')
    if not Semester.objects.exists():
        for year, semester in zip(YEAR_CHOICES, SEMESTER_CHOICES):
            Semester.objects.create(year=year[0], semester=semester[0])

def initialize_courses(apps, schema_editor):
    Course = apps.get_model('usermodule', 'Courses')
    if not Course.objects.exists():
        for dept in DEPT_CHOICES:
            Course.objects.create(course_name=dept[0])


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'HOD'), (2, 'Staff'), (3, 'Student')], default=1, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('1st', '1st Semester'), ('2nd', '2nd Semester'), ('3rd', '3rd Semester'), ('4th', '4th Semester'), ('5th', '5th Semester'), ('6th', '6th Semester')], max_length=100)),
                ('year', models.CharField(choices=[('1st', '1st Semester'), ('2nd', '2nd Semester'), ('3rd', '3rd Semester'), ('4th', '4th Semester'), ('5th', '5th Semester'), ('6th', '6th Semester')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reg_id', models.CharField(max_length=10)),
                ('photo', models.FileField(upload_to=usermodule.models.Student.wrapper)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usermodule.courses')),
                ('sem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usermodule.semester')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usermodule.courses')),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HOD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hod', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(initialize_semesters),
        migrations.RunPython(initialize_courses),
    ]
