from django import forms
from .models import Post, Comment
from taggit.forms import TagField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "text",
            "tags"
        ]
        tags=TagField(label='Tags')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text'
        ]