from .models import Comment
from django import forms

# Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

     