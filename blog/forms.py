from django import forms

from .models import Comment
from .models import About


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['text', 'thumb']
