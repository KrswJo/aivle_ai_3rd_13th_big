from django.shortcuts import render,redirect, get_object_or_404
from .models import Board
from .forms import RegistForm
from django.core.paginator import Paginator

def index(request):
    page = request.GET.get('page', '1')  # 페이지 파라미터 얻기, 없으면 1
    board_list = Board.objects.order_by('-id')
 
    # 페이징 처리
    paginator = Paginator(board_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)  # page에 해당하는 페이징 객체 생성

    context = {'board_list': page_obj}   # 페이징 객체(page_obj) 전달
    return render(request, 'boards/index.html', context)


def new(request):
    if request.method == 'POST':
        form = RegistForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('boards:index')
    else:
        form = RegistForm()
    context = {'form': form,}
    return render(request, 'boards/new.html', context)

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.user
        contents = request.POST.get('contents')
        nickname = request.user.nickname
        Board.objects.create(title=title, author=author, contents=contents, nickname = nickname)
        return redirect('boards:index')


def edit(request, pk):
    post = get_object_or_404(Board, id=pk)
    if request.method == 'POST':
        form = RegistForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('boards:index')
    else:
        form = RegistForm(instance=post)
    context = {'form': form,}
    return render(request, 'boards/edit.html', context)

def delete(request, pk):
    post = get_object_or_404(Board, id=pk)
    post.delete()
    return redirect('boards:index')

def detail(request, pk):
    board_list = get_object_or_404(Board, id=pk)
    context = {'board_list': board_list}
    return render(request, 'boards/detail.html', context)