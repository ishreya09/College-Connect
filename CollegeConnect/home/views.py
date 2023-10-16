from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request, 'home/home.html', context)

def privacypolicy(request):
    context = {}
    return render(request, 'home/privacypolicy.html', context)

def contact_us(request):
    context={}
    return render (request,'home/contactus.html',context)

def contact_success(request):
    context={}
    return render (request,'home/contactsuccess.html',context)

def about_us(request):
    context={}
    return render(request,'home/aboutus.html',context)

def copyright(request):
    context={}
    return render(request,'home/copyright.html',context)


def error_404(request):
    context ={}
    return render(request, 'home/error404.html',context)

