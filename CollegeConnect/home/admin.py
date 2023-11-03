
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import SendEmailForm

from django.contrib import admin
from .models import *


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'query', 'sent_on']
    search_fields = ['name', 'email', 'query']
    list_filter = ['sent_on']
    readonly_fields = ('name', 'email', 'query', 'sent_on')

    
# Register the ContactUs model with the custom admin class
admin.site.register(ContactUs, ContactUsAdmin)
