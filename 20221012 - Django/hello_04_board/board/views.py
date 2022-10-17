from django.shortcuts import render,render,redirect
from .models import Blog

# Create your views here.
def index(request):
    ctx = {'msg' : 'Welcome 장고'}
    return render(request, 'board/index.html', ctx)

def board_create(request):
    if request.method == 'POST': # POST방식 요청?
        post_data = request.POST #입력데이터
        board = Blog(
            title=request.POST['title'],
            content=request.POST['content']
        )
        board.save()
        return redirect('main')

    # GET방식
    return render(request, "board/create.html")

def board_list(request):
    board_list = Blog.objects.all() # DB내용 다 가져옴
    ctx = {'brd_list' : board_list}
    return render(request, 'board/list.html',ctx)