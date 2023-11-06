from django import forms
from .models import ClubMember

class ClubMembershipApplicationForm(forms.ModelForm):
    class Meta:
        model = ClubMembershipApplication
        fields = ['club', 'additional_information']
        widgets = {
            'additional_information': forms.Textarea(attrs={'rows': 3}),
        }