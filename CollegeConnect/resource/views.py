from django.shortcuts import render

# Create your views here.
def resource(request):
    context={}
    return render(request, 'resource/resource.html',context)