from django.shortcuts import render
from django.shortcuts import redirect

from .forms import PostForm
from .models import *

from django.contrib import messages
import re
from taggit.models import Tag


# Create your views here.
def create_slug(username,title):
    # remove all special character except space
    slug = re.sub(r'[^a-zA-Z0-9\s]', '', title)
    # replace all space with -
    slug= username+" "+slug
    slug = slug.lower()
    slug = re.sub(r'\s', '-', slug)
    return slug

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
            # get branches
            branches = form.cleaned_data['branch']
            # get tags
            tags = form.cleaned_data['tags']
            print(branches,tags)
            # get title
            title = form.cleaned_data['title']

            # create slug
            slug = create_slug(username,title)

            post = form.save(commit=False)
            post.user = User.objects.get(username=username)
            post.author = post.user.first_name+" "+post.user.last_name
            post.slug = slug
            post.save()
            # add branches
            for branch in branches:
                post.branch.add(branch)
            # add tags
            for tag in tags:
                tag = tag.strip().lower()
                domain, created = Tag.objects.get_or_create(name=tag)
                post.tags.add(tag)
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

