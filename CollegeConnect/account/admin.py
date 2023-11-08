from django.contrib import admin

# Register your models here.
from .models import *
from taggit.models import Tag 
from django.urls import reverse
from django.utils.html import format_html
class StudentAdmin(admin.ModelAdmin):
    list_display=(
        'student_id',
        'user',
        'department',
        'branch',
        'college_email',
        'is_mentor',
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
        "is_mentor",
    ]
    list_filter=[
        'department',
        'is_mentor',
        'email_confirmed',
        'show_number',
        'year_of_passing_out',
        
    ]

class MentorAdmin(admin.ModelAdmin):
    actions = [
        'remove_not_approved_mentors_action_six_months',
        'remove_not_approved_mentors_action_one_day',  
    ]

    list_display=(
        'student',
        'username',
        'approved',
        'resume',
        'list_domains',
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
        'approved',
        'last_application_date'
        
    ]

    def list_domains(self, obj):
        # Retrieve the list of domain tags for the mentor and return them as a string
        domain_tags = obj.domain.all()  # Assuming 'domain' is the name of the TaggableManager field
        return ', '.join(tag.name for tag in domain_tags)

    list_domains.short_description = "Domains"  # Set a custom column header for the domains

    def remove_not_approved_mentors_action_six_months(self, request, queryset):
        return format_html('<a class="button" href="/account/mentor/remove_not_approved_six_months">Remove not approved Mentors for over 6 months</a>')
    remove_not_approved_mentors_action_six_months.short_description = "Remove Not Approved Mentors for over Six months"
    
    def remove_not_approved_mentors_action_one_day(self, request, queryset):
        return format_html('<a class="button" href="/account/mentor/remove_not_approved_one_day">Remove not approved Mentors for over 6 months</a>')
    remove_not_approved_mentors_action_one_day.short_description = "Remove Not Approved Mentors for over One day"


class ClubAdmin(admin.ModelAdmin):
    list_display= (
        'club_name',
        'club_desc',
        # 'list_branch',
    )

    search_fields=[
        'branch',
        'club_name',
        'club_desc',
    ]

    list_filter=[
        'branch',
    ]

    list_editable=[
        'club_desc',   
    ]

    def list_branch(self, obj):
        # Retrieve the list of domain tags for the mentor and return them as a string
        branch = obj.branch.all()  # Assuming 'domain' is the name of the TaggableManager field
        return ', '.join(b.branch_name for b in branch)

    list_branch.short_description = "branches"  # Set a custom column header for the domains

# clubmember admin

class ClubMemberAdmin(admin.ModelAdmin):
    list_display= (
        'user',
        'club',
        'club_head',
        'social_media_manager',
        'joined_on',
    )

    search_fields=[
        'user',
        'club',
    ]

    list_filter=[
        'club',
        'club_head',
        'social_media_manager',
    ]

    list_editable=[
        'club_head',
        'social_media_manager',
    ]
    

admin.site.register(Student,StudentAdmin)
admin.site.register(Mentor,MentorAdmin)
admin.site.register(Club,ClubAdmin)
admin.site.register(ClubMember,ClubMemberAdmin)