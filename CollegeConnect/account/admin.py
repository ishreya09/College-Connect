from django.contrib import admin

# Register your models here.
from .models import *

class StudentAdmin(admin.ModelAdmin):
    list_display=(
        'student_id',
        'user',
        'department',
        'branch',
        'college_email',
        'is_mentor',
        'show_number',
        'email_confirmed',
        'year_of_passing_out',

    )
    search_fields=[
        'department',
        'branch',
        'student_id',
        'user',
        'college_email',
        'whatsapp_number',

    ]
    list_editable= [
        'is_mentor',
        'show_number',
        'email_confirmed',
    ]
    list_filter=[
        'department',
        'branch',
        'student_id',
        'user',
        'college_email',
        'whatsapp_number',
        'is_mentor',
        'email_confirmed',
        'show_number',
        'year_of_passing_out',
        
    ]


class MentorAdmin(admin.ModelAdmin):
    list_display=(
        'student',
        'username',
        'approved',
        'domain'
    )
    search_fields=[
        'student',
        'username',
        'approved',
        'domain'
    ]
    list_editable= [
        'approved'
    ]
    list_filter=[
        'domain',
        'approved'
        
    ]


admin.site.register(Student,StudentAdmin)
admin.site.register(Mentor,MentorAdmin)