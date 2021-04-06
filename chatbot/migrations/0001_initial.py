# Generated by Django 2.2.4 on 2021-04-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=255)),
                ('course_dept', models.CharField(max_length=255)),
                ('course_type', models.CharField(max_length=255)),
                ('course_credit', models.CharField(max_length=255)),
                ('course_title', models.CharField(max_length=255)),
                ('course_year', models.IntegerField()),
                ('course_sems', models.CharField(max_length=255)),
                ('professor_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('user_dept', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('course_id', models.CharField(max_length=255)),
                ('course_title', models.CharField(max_length=255)),
                ('course_year', models.IntegerField()),
                ('course_sems', models.CharField(max_length=255)),
                ('course_dept', models.CharField(max_length=255)),
                ('course_grade', models.IntegerField()),
                ('course_credit', models.CharField(max_length=255)),
            ],
        ),
    ]
