from django.forms.models import ModelForm
from django import forms
from commentapp.models import Comment

class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        # 코멘트 입력 폼 설정
        widgets = { 
            'content': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Write a comment...',
                'style': 'resize: vertical;'
            }),
        }