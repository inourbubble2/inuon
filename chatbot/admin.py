from django.contrib import admin
from .models import User, UserCourse, CourseList

# Register your models here.
admin.site.register(User)
admin.site.register(UserCourse)
admin.site.register(CourseList)
