from django.shortcuts import render
from .models import Department

def department_tree_view(request):
    departments = Department.get_root_nodes()
    return render(request, 'employees/department_tree.html', {'departments': departments})
