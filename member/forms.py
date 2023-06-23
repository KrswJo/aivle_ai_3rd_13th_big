# forms.py

from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname","costco_id","english_name","card_validity_period"]

    def signup(self, request, user):
        user.nickname = self.cleaned_data["nickname"]
        user.costco_id = self.cleaned_data["costco_id"]
        user.english_name = self.cleaned_data["english_name"]
        user.card_validity_period = self.cleaned_data["card_validity_period"]
        user.save()