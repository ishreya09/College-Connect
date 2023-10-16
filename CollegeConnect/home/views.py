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

