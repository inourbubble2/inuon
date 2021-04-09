import logging

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, JsonResponse

from . import chats, crawls, users


logger = logging.getLogger(__name__)


# GET /answer
# parameter: username, content
# return: 해당 유저의 정보를 기반으로 질문의 답을 반환
def answer(request):
    if request.method == 'GET':  # Get 방식만 허용됨
        uname = request.GET.get('username', '')
        content = request.GET.get('content', '')

        # Parameter가 정상적인지 확인
        if uname == '' or content == '':
            return HttpResponse('Invalid Parameter', 400)

        res = chats.get_response(uname, content)

        return JsonResponse({"res": res},
                            status=200,
                            json_dumps_params={"ensure_ascii": False})

    else:
        return HttpResponse('Invalid Request Type', status=400)


# GET /user
# parameter: username
# return: 해당 유저의 이름, 학과 정보를 반환
def user(request):
    if request.method == 'GET':
        uname = request.GET.get('username', '')
        u = users.select_user_by_id(uname)

        if u is not False:
            return JsonResponse({"user": u.user_id,
                                 "name": u.user_name,
                                 "dept": u.user_dept},
                                status=200,
                                json_dumps_params={"ensure_ascii": False})
        else:
            return HttpResponse("User does not exist.", status="400")

    elif request.method == 'PUT':
        pass
    elif request.method == 'PATCH':
        pass
    elif request.method == 'DELETE':
        pass

    return HttpResponse("You can join here.")


# GET /usercourse?username=
# -> parameter: username
# -> return: 이미 저장된 user의 강의 목록
# POST /usercourse
# -> Parameter: Http Request의 Body에 username과 password를 저장하여 전송함)
# -> return: 해당 user의 강의 목록 크롤링하여 저장한 후 반환
@csrf_exempt
def usercourse(request):
    if request.method == 'GET':
        uname = request.GET.get('username', '')
        course = []
        u = users.select_user_by_id(uname)
        ucs = users.select_usercourse_by_id(uname)

        if ucs is not False:
            for uc in ucs:
                course.append([uc.course_id,
                               uc.course_title, uc.course_dept,
                               uc.course_year, uc.course_sems,
                               uc.course_credit, uc.course_grade])

            return JsonResponse({"user": uname,
                                 "name": u.user_name,
                                 "dept": u.user_dept,
                                 "course": course},
                                status=200,
                                json_dumps_params={"ensure_ascii": False})
        else:
            return HttpResponse("User does not exist.", status="400")
    elif request.method == 'POST':
        uname = request.POST.get('username')
        pword = request.POST.get('password')

        # Parameter가 정상적인지 확인
        if uname == '' or pword == '':
            return HttpResponse('Invalid Parameter', 400)

        if uname is None or pword is None:
            return HttpResponse('Invalid Parameter', 400)

        c = crawls.Crawl(uname, pword)
        c.login()

        try:
            # TODO : 데이터베이스 설계 완료 시, 크롤링한 데이터는 저장만 하고
            #        Response는 200/400으로 단순하게 성공 여부만 알려줄 것
            name, dept = c.get_info()  # {"name": name.text, "dept": dept.text}
            course = c.get_class()  # [[year, sem_t, course_name, course_code]]

            users.insert_user(uname, name, dept)
            users.insert_course(uname, course)

            return JsonResponse({"name": name, "dept": dept, "course": course},
                                status=200,
                                json_dumps_params={"ensure_ascii": False})
        except Exception:  # 크롤링 중 에러가 발생한다면 로그인 정보가 틀린 것
            return HttpResponse("Login failed.", status=400)
    elif request.method == 'PUT':
        pass
    elif request.method == 'PATCH':
        pass
    elif request.method == 'DELETE':
        pass

    return HttpResponse('You can manage course here.')


# calendar(): GET, PUT, PATCH, DELETE
# TODO : 일정(캘린더)의 조회, 입력, 수정, 삭제를 담당하는 메소드 작성
def calendar(request):
    return HttpResponse("You can get calendar here.")