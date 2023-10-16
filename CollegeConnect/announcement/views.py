from django.shortcuts import render

# Create your views here.
def announcement(request):
    context={}
    return render(request, 'announcement/announcement.html',context)