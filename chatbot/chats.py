# 질문으로 정규표현식 처리하는 곳
# get_response() 에 질문이 파라미터로 주어진다
# 정규표현식으로 처리한 뒤
# 답변을 get_response() 마지막에 return하면 됨
def get_response(uname, content):
    return 'Hello, ' + uname + '. your question was ' + content
