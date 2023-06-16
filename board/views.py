from django.shortcuts import render,redirect, get_object_or_404
from .models import Board,Comment
from .forms import RegistForm,CommentForm
from django.core.paginator import Paginator
import logging


logger = logging.getLogger('request_logger')

def index(request):
    # 페이지 파라미터 얻기, 없으면 1
    page = request.GET.get('page', '1')
    board_list = Board.objects.order_by('-id')
 

    # 페이지당 10개씩 보여주기
    paginator = Paginator(board_list, 10)
    page_obj = paginator.get_page(page)

    context = {'board_list': page_obj}
    return render(request, 'boards/index.html', context)


def new(request):
    if request.method == 'POST':
        form = RegistForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('boards:detail', post.pk)
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
    post = get_object_or_404(Board, pk=pk)
    if request.user == post.author:
        if request.method == 'POST':
            form = RegistForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('boards:detail', post.pk)
        else:
            form = RegistForm(instance=post)
    else:
        return redirect('boards:index')
    context = {
        #'board': boards,
        'form': form,
    }
    return render(request, 'boards/edit.html', context)


def delete(request, pk):
    post = get_object_or_404(Board, id=pk)
    if request.user.is_authenticated:
        if request.user == post.author: 
            post.delete()
            return redirect('boards:index')
    
    return redirect('boards:detail', post.pk)


def detail(request, pk):
    board_list = get_object_or_404(Board, pk=pk)
    comment_list = Comment.objects.filter(board=board_list)
    context = {'board_list': board_list, "comments": comment_list}
    return render(request, 'boards/detail.html', context)

def comments_create(request, pk):
    if request.user.is_authenticated:
        board = get_object_or_404(Board, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.board = board
            comment.nickname = request.user.nickname
            comment.user_id = request.user.pk
            comment.save()
        return redirect('boards:detail', board.pk)
    return redirect('boards:new.html')


def comments_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('boards:detail', pk)