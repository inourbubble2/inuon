from .models import User, UserCourse
import logging


logger = logging.getLogger(__name__)


# Database에 새로운 유저 정보 저장하기
def insert_user(uname, name, dept):
    try:
        if select_user_by_id(uname):
            logger.info("User has been already saved")
        else:
            u = User(user_id=uname, user_name=name, user_dept=dept)
            u.save()
    except Exception as e:
        logger.info(e)


def insert_course(uname, course):
    try:
        if select_usercourse_by_id(uname):
            logger.info("User courses have been already saved")
        else:
            for c in course:  # year, sem_t, course_name, course_code
                year = c[0]
                sems = c[1]
                name = c[2]
                code = c[3]

                UserCourse(user_id=uname,
                           course_id=code,
                           course_title=name,
                           course_year=year,
                           course_sems=sems,
                           course_dept='',
                           course_grade=0,
                           course_credit='').save()
    except Exception as e:
        logger.info(e)


def select_user_by_id(uname):
    if uname == '':
        return False
    try:
        u = User.objects.get(user_id=uname)
        return u
    except Exception as e:
        logger.info(e)
        return False


def select_usercourse_by_id(uname):
    if uname == '':
        return False
    try:
        uc = UserCourse.objects.filter(user_id=uname)
        return uc
    except Exception as e:
        logger.info(e)
        return False

