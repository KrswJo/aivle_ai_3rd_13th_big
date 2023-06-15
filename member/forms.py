# forms.py

from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]
        # fields = ["nickname","country"]

    def signup(self, request, user):
        user.nickname = self.cleaned_data["nickname"]
        # user.country = self.cleaned_data["country"]
        user.save()