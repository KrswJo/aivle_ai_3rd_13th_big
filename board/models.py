from django.db import models

class Board(models.Model):
    title       = models.CharField(max_length=200, verbose_name="제목")
    contents    = models.TextField(verbose_name="내용")
    author      = models.ForeignKey("member.User", on_delete = models.CASCADE)
    hit         = models.PositiveIntegerField(default = 0)
    created_date  = models.DateTimeField(auto_now_add=True)
    published_date  = models.DateTimeField(auto_now=True, verbose_name="최종수정일")
    nickname    = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()
        
class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey("member.User", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    contents = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contents