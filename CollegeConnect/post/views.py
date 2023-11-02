from django.shortcuts import render
from django.shortcuts import redirect
from .forms import PostForm

# Create your views here.

def feed(request):
    context={}
    return render(request, 'post/feed.html',context)

def make_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            pass
            # Process the form data, save the Post object, etc.
            # Example: post = form.save()
            # You can customize this based on your requirements.
        
        return redirect("/post/feed")
    form = PostForm()    
    # print("Hello")
    context={
        'form':form
    }
    return render(request,'post/make_post.html',context)

def post_detail(request,slug=None):
    context={}
    return render(request,'post/post_detail.html',context)

