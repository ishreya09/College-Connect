from django.shortcuts import render

# Create your views here.
def club(request):
    context={}
    return render(request, 'club/club.html',context)