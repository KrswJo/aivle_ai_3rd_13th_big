from django.shortcuts import render
from django.views.generic import ListView
from .models import News
from board.models import Board

class NewsList(ListView):
    model = News
    ordering = '-pk'
    template_name = 'main/news_list.html'

    def get(self, request, *args, **kwargs):
        board = Board.objects.all().order_by('-hit', '-created_date')
        return render(request, self.template_name, {'board_list': board})
