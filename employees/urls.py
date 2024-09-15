from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.department_tree_view, name='department_tree'),
]
