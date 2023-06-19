from django import forms
from django.forms import widgets
from .models import Board,Comment

class RegistForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'contents']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'contents': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['contents']