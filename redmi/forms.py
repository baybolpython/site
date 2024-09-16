from django import forms
from .models import Redmi
from .models import Comment
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
#
#
# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
#

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Поля формы (только текст комментария)


class RedmiForm(forms.ModelForm):

    class Meta:
        model = Redmi
        fields = '__all__'

