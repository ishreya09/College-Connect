from django.urls import path
from .views import get_branches

urlpatterns = [
    path('<department_id>', get_branches, name='get_branches'),
]
