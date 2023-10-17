from django.shortcuts import render

# Create your views here.
from .models import Branch
from django.http import JsonResponse

def get_branches(request, department_id):
    branches = Branch.objects.filter(department_id=department_id).values('branch_code', 'branch_name')
    return JsonResponse({'branches': list(branches)})