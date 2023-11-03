from django.shortcuts import render
from django.shortcuts import redirect

from .forms import PostForm
from .models import *

from django.contrib import messages


# Create your views here.

def feed(request):
    username=request.user.__str__()
    if(username=="AnonymousUser"):
        messages.error(request,"Please sign in first")
        return redirect("/account/login" )
    context={}
    return render(request, 'post/feed.html',context)

def make_post(request):
    username=request.user.__str__()
    if(username=="AnonymousUser"):
        messages.error(request,"Please sign in first")
        return redirect("/account/login" )    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = User.objects.get(username=username)
            post.author = post.user.first_name+" "+post.user.last_name
            post.save()
            messages.success(request, "Post successfully created!")
            return redirect("/post/feed")
        else:
            messages.error(request, "Error in form submission. Please correct the errors below.")
    
    form = PostForm()    
    # print("Hello")
    context={
        'form':form
    }
    return render(request,'post/make_post.html',context)

def post_detail(request,slug=None):
    username=request.user.__str__()
    if(username=="AnonymousUser"):
        messages.error(request,"Please sign in first")
        return redirect("/account/login" )    
    context={}
    return render(request,'post/post_detail.html',context)

