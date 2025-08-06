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
                'placeholder': '댓글을 입력하세요...',
                'style': 'resize: vertical;'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # 댓글 폼에 필요한 필드만 넣기