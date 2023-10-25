from django.shortcuts import render
from .models import ContactUs
# Create your views here.
def home(request):
    context={}
    return render(request, 'home/home.html', context)

def privacypolicy(request):
    context = {}
    return render(request, 'home/privacypolicy.html', context)

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name',False)
        email = request.POST.get('email',False)
        query = request.POST.get('query',False)
        if not name:
            messages.error(request, 'Name is required.')
        if not email:
            messages.error(request, 'Email is required.')
        if not query:
            messages.error(request, 'Query is required.')
        if name and email and query:
            ContactUs.objects.create(name=name, email=email, query=query)
            return redirect ('/contact-success')
        else:
            return redirect('/contact-us')
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

