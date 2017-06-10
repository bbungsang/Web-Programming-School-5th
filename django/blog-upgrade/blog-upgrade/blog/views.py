from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html') # 반드시 앱 이름을 쓰고 그 뒤에 파일명 쓰기

def post_new():
    pass

def post_detail():
    pass

def post_edit():
    pass

def post_delete():
    pass

def comment_list():
    pass

def comment_edit():
    pass

def comment_delete():
    pass
