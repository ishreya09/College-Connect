from django.shortcuts import render
from django.shortcuts import redirect

from .models import Announcement

from django.contrib import messages

# Create your views here.
def announcement(request):
    username=request.user.__str__()
    if(username=="AnonymousUser"):
        messages.error(request,"Please sign in first")
        return redirect("/account/login" )  

    # retrive all   
    announcements = Announcement.objects.all()

    context={'announcements':announcements}
    return render(request, 'announcement/announcement.html',context )