from django.shortcuts import render

# Create your views here.
def index(request):
    # http://localhost:/blog/
    # 필요한 작업 코드 작성
    # html 경로 반환
    return render(request, 'blog/index.html', {'msg' : '헬로~'})w