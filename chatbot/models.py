from django.db import models


class CourseList(models.Model):
    course_id = models.CharField(max_length=255)
    course_dept = models.CharField(max_length=255)
    course_type = models.CharField(max_length=255)
    course_credit = models.CharField(max_length=255)
    course_title = models.CharField(max_length=255)
    course_year = models.IntegerField()
    course_sems = models.CharField(max_length=255)
    professor_name = models.CharField(max_length=255)


class UserCourse(models.Model):
    user_id = models.CharField(max_length=255)
    course_id = models.CharField(max_length=255)
    course_title = models.CharField(max_length=255)
    course_year = models.IntegerField()
    course_sems = models.CharField(max_length=255)
    course_dept = models.CharField(max_length=255)
    course_grade = models.IntegerField()
    course_credit = models.CharField(max_length=255)


class User(models.Model):
    user_id = models.CharField(max_length=255)
    user_dept = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)