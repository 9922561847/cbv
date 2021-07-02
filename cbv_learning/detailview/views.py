from django.shortcuts import render

from django.views.generic.detail import DetailView 
from django.views.generic.list import ListView

from .models import Student

class StudentDetailView(DetailView):
    model = Student
    template_name = 'detailview/studentdetailview.html'
    context_object_name = 'my_favorites'
    pk_url_kwarg = 'id'

class StuListView(ListView):
    model = Student
    template_name = 'detailview/stulistview.html'
