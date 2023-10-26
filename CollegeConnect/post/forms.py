from .models import Post
from django import forms
from ckeditor.widgets import CKEditorWidget



class PostForm(forms.ModelForm):
    content= forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = (
        'title',
        'featured_image',
        'content',
        'tags',
        'branch',
        )
