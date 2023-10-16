from django.shortcuts import render

# Create your views here.

def register(request):
    context={}
    return render(request, 'account/register.html',context)

def login(request):
    context={}
    return render(request, 'account/login.html',context)

def profile(request):
    context ={}
    return render(request, 'account/profile.html',context)

def change_password(request):
    context ={}
    return render(request, 'account/change_password.html',context)

def edit_profile(request):
    context ={}
    return render(request, 'account/editprofile.html',context)