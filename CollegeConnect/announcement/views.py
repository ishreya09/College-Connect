from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

# Create your views here.
def announcement(request):
    username=request.user.__str__()
    if(username=="AnonymousUser"):
        messages.error(request,"Please sign in first")
        return redirect("/account/login" )    
    context={}
    return render(request, 'announcement/announcement.html',context)