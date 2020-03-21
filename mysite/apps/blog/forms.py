from django import forms
from .models import Post, Comment
from taggit.forms import TagField
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "text",
            "tags",
        ]
        tags=TagField(label='Tags')
        widgets = {
            'text': SummernoteWidget (attrs={
                'summernote': {
                    'airMode': False,
                    'width': '90%',
                    'height': '300',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['font', ['strikethrough', 'superscript', 'subscript']],
                        ['fontsize', ['fontsize']],
                        ['color', ['color']],
                        ['para', ['ul', 'ol', 'paragraph']],
                        ['height', ['height']],
                        ['misc', ['codeview']],
                        ['insert', ['link', 'picture']],
                    ],

                },

            }),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text'
        ]
        widgets = {
            'text': SummernoteWidget (attrs={
                'summernote': {
                    'airMode': False,
                    'width': '90%',
                    'height': '300',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['font', ['strikethrough', 'superscript', 'subscript']],
                        ['fontsize', ['fontsize']],
                        ['color', ['color']],
                        ['para', ['ul', 'ol', 'paragraph']],
                        ['height', ['height']],
                        ['misc', ['codeview']],
                    ],

                },

            }),

        }