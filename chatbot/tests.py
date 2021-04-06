from django.test import TestCase
from .users import insert_course
from .models import User, UserCourse


# Create your tests here.
class UserModelTests(TestCase):
    def test_create_user(self):
        uname = 'test'
        name = 'test123'
        dept = 'test456'
        u = User(user_id=uname, user_name=name, user_dept=dept)
        u.save()
        print(u)
        self.assertIs(u.user_id, 'test')

    def test_select_user(self):
        print(User.objects.all())

    def test_create_usercourse(self):
        uname = '201802904'
        course = [[2020, '1학기', '프로그래밍입문', '0003426003'],
                  [2020, '1학기', 'Java언어', '0003428001'],
                  [2020, '1학기', '대학영어회화1', '0005060106'],
                  [2020, '1학기', '디지털공학', 'IAA6005001'],
                  [2020, '1학기', '데이터통신', 'IAA6014003'],
                  [2020, '1학기', '운영체제', 'IAA6018001'],
                  [2020, '여름학기', '데이터베이스', '0001770002']]
        insert_course(uname, course)
        print(UserCourse.objects.all())