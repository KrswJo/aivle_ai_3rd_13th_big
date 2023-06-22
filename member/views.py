from django.shortcuts import render
from django.db import connection
from .models import User

# Create your views here.
def mypage(request):
        # member_user 테이블의 레코드를 가져와서 객체로 다룹니다.
    current_user = User.objects.get(pk = request.user.pk) #username: janggh1012
    
    
    
    
    
    
    context = {'current_user': current_user}

    return render(request, 'account/mypage.html',context)