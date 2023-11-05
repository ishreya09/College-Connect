from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


login_required(login_url='/account/login')
def resource(request):
    context={}
    return render(request, 'resource/resource.html',context)