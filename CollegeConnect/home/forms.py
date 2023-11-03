from django import forms

# Define a form for sending emails
class SendEmailForm(forms.Form):
    reciever= forms.CharField(widget=forms.Textarea,help_text="DO NOT CHANGE")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
