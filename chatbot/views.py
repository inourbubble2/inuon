from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from django.core import serializers

from . import chats, crawls, users
import json


# ask(): GET
# example query: /chatbot/ask?id=201800000&content=수강%20신청%20언제야?
# request = {
#   'username': '201800000'
#   'content': '수강 신청 언제야?'
# }
# return {
# "res": '수강 신청은 X월 X일 입니다.'
# } : JSON Object
def ask(request):
    if request.method == 'GET': # Get 방식만 허용됨
        uname = request.GET.get('username','')
        content = request.GET.get('content','')

        # Parameter가 정상적인지 확인
        if uname == '' or content == '':
            return HttpResponse('Invalid Parameter', 400)

        # 가입된 학번인지 체크
        if not users.is_valid_id(uname):
            return HttpResponse('Invalid ID', 400)

        res = chats.get_response(uname, content)
        return JsonResponse({"res":res}, status=200, json_dumps_params = {"ensure_ascii": False})

    else:
        return HttpResponse('Invalid Request Type', status=400)


# crawl(): POST
# JSON 형식으로 객체를 받는다
# 객체는 Key:Value의 딕셔너리
# {
#   username: '2018'
#   password: '1234'
# } : JSON Object
def crawl(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Parameter가 정상적인지 확인
        if len(data.keys()) < 2:
            return HttpResponse('Invalid Parameter', status=400)
        for value in data.values():
            if value in '':
                return HttpResponse('Invalid Parameter', status=400)
        
        uname = data['username']
        pword = data['password']

        c = crawls.Crawl(uname, pword)
        c.login()

        try:
            # TODO : 데이터베이스 설계 완료 시, 크롤링한 데이터는 저장만 하고
            #        Response는 200/400으로 단순하게 성공 여부만 알려줄 것
            return JsonResponse({"info":c.get_info(), "course":c.get_class()}, status=200, json_dumps_params = {"ensure_ascii": False})
        except Exception: # 크롤링 중 에러가 발생한다면 로그인 정보가 틀린 것
            return HttpResponse("Login failed.", status=400)
    else:
        return HttpResponse('Invalid Request Type', status=400)


# user(): PUT, PATCH, DELETE
# TODO: 유저 목록의 입력, 수정, 삭제를 담당하는 메소드 작성
def user(request):
    return HttpResponse("You can join here.")


# course(): GET, PUT, PATCH, DELETE
# TODO : 강의 목록의 조회, 입력, 수정, 삭제를 담당하는 메소드 작성
def course(request):
    if request.method == 'GET':
        pass
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