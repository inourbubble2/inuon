import re


# 질문으로 정규표현식 처리하는 곳
# get_response() 에 질문이 파라미터로 주어진다
# 정규표현식으로 처리한 뒤
# 답변을 get_response() 마지막에 return하면 됨
def get_response(content):
    # checked_str = check_spell(in_str)
    return _get_response(content)


major_list = ['국어국문', '영어영문', '독어독문', '불어불문', '일어일문', '중어중국', '수학과',
              '물리학과', '화학과', '패션산업', '해양학과', '사회복지학과', '신문방송', '문헌정보', '창의인재개발',
              '행정학과','정치외교','경제학과','무역학','소비자','기계공학','전기공학','전자공학','산업경영',
              '신소재','안전공학','에너지화학','메카트로닉스공학','컴퓨터공학','정보통신공학','임베디드시스템공학',
              '경영','세무회계','조형예술','디자인','공연예술','체육','운동건강','사범대',
              '국어교육','영어교육','일어교육','수학교육','체육교육','유야교육','역사교육','윤리교육',
              '도시행정','도시환경','도시공학','도시건축'
              '생명과학부', '생명공학부', '동북아국제통상']


# 수강에 관련된 request 처리
def main_sugang(in_str):
    is_about_history = False
    is_about_ban = False
    # is_about_enable = False
    is_about_dis = False

    history_keyword = ['수강한', '수강했', '들은', '들었', '내역', '기록']
    ban_keyword = ['못듣는', '못', '제한', '없는']
    dis_keyword = ['장애', '도우미']

    for pat in history_keyword:
        if pat in in_str:
            is_about_history = True
            break

    for ban in ban_keyword:
        if ban in in_str:
            is_about_ban = True
            break

    for dis in dis_keyword:
        if dis in in_str:
            is_about_dis = True
            break

    if is_about_history:
        return '여태껏 수강한 내역 보여주기'
    elif '포기' in in_str:
        return f2_sugang()
    elif is_about_ban:
        return f3_sugang()
    elif '최대' in in_str:
        return f4_sugang()
    elif is_about_dis:
        return f5_sugang()
    else:
        return f1_sugang()


def f1_sugang():  # 수강 신청 통합 정보 제공
    return '''수강신청 장바구니 기간 : 2021. 2. 9.(화) 10:00 ～ 2.10(수) 17:00\n
           󰏚 수강신청 기간\n
           m 2,3,4학년(재학생,복학생,재입학생,기존 교환학생)\n
           - 학번 끝자리가 짝수인 학생 : 2021. 2.18.(목) 10:00～13:00, 2021. 2.19.(금) 10:00～2.22.(월) 17:00\n
           - 학번 끝자리가 홀수인 학생 : 2021. 2.18.(목) 14:00～17:00, 2021. 2.19.(금) 10:00～2.22.(월) 17:00'''


def f2_sugang():  # 수강 포기
    return '수강 포기관련 교칙 제공'


def f3_sugang():  # 수강 제한
    return '수강 제한 과목'


def f4_sugang():  # 수강신청 최대학점
    return '수강신청 최대 학점'


def f5_sugang():  # 장애학생 수강신청
    return '장애.도우미 선 수강신청'


def re_course():  # 재수강, 재이수
    return '재수강, 재이수'


# 학점에 관련된 request 처리
def req_credits(in_str):  # 학점 현황
    return '학점 현황 보여주기'


def req_state(in_str):  # 휴,복학 안내
    if re.search('군|군대|입대', in_str):
        return req_army_absence()
    else:
        return '휴,복학 공지사항 안내'


def req_sub_major():  # 부, 복수 전공
    return '부,복수 전공 안내'


def req_link_major():  # 연계 전공
    return '연계 전공 안내'


def req_army_absence():
    return '군휴학 안내'


def change_major(in_str):

    if re.search('기간|날짜|언제', in_str):
        return change_major_period()
    else:
        return change_major_conditions()


def change_major_conditions():
    return '전과 학칙 제공'


def change_major_period():
    return '전과 기간 공지사항'


def req_penalty():
    return '학사 징계 안내'


def req_graduation(in_str):

    for major in major_list:
        if major in in_str:
            # major 값 갖고 db에서 해당하는 학과 졸업학점 찾아 전달하기
            answ = major + "학과 졸업 학점은 " + "입니다."
            return answ

    if re.search('조기', in_str):
        return "신청자격 : 2학년 2학기(4학기)까지의 총성적 평점평균이 4.0이상인 자\n" \
               "신청기간 : 3학년 1학기(5학기) 개시 전 소정의 기간(학사일정을 참조)\n" \
               "신청방법 : 인터넷 신청(포탈/통합정보/졸업/조기졸업신청)\n" \
               "졸업요건 : 6개 학기 또는 7개 학기에 졸업요건을 갖추고 성적 평점평균 4.0이상인 경우에 조기졸업 인정"
    #elif re.search('과$|......대')
    else:
        return '졸업 요건 및 자격 안내'


def _get_response(in_str):
    if re.search('재수강|재이수', in_str):
        return re_course()
    elif re.search('졸업|수료', in_str):
        return req_graduation(in_str)
    elif re.search('수강|강의|장바구니', in_str):
        return main_sugang(in_str)  # 강의, 수강으로 나누기
    elif re.search('장애', in_str):
        return f5_sugang()
    elif re.search('학점', in_str):
        return req_credits(in_str)
    elif re.search('휴학|복학', in_str):
        return req_state(in_str)
    elif re.search('부전공|복수전공|부복수전공', in_str):
        return req_sub_major()
    elif re.search('전과', in_str):
        return change_major(in_str)
    elif re.search('연계', in_str):
        return req_link_major()
    elif re.search('징계|경고', in_str):
        return req_penalty()
    else:
        return "무슨 말인지 모르겠습니다."
