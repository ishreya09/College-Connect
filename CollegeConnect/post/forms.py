from .models import Post
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.forms import CheckboxSelectMultiple

from branch.models import Branch
import markdown


class PostForm(forms.ModelForm):
    content= forms.CharField(widget=CKEditorWidget(config_name='default'))

    branch = forms.ModelMultipleChoiceField(
        queryset=Branch.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Use checkboxes for multiple selections
        required=True  
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Fetch the Branch model objects and convert them to markdown
        # branch_objects = Branch.objects.all()
        # branch_choices = [(branch.branch_code, markdown.markdown(branch.branch_name)) for branch in branch_objects]
        
        # # Add the branch objects as markdown choices for your form field
        # self.fields['branch'].choices = branch_choices

    class Meta:
        model = Post
        fields = (
        'title',
        'content',
        'tags',
        'branch',
        )
        