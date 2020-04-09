from django import forms
from .models import Post, Comment
from django.forms.widgets import HiddenInput

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title', 'author', 'text','image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'post'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('author','text','post')
        widgets = {}
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'comment'}),
            'post': forms.HiddenInput()
        }
            