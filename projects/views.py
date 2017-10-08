from django.shortcuts import render

from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Project, Budget, Entry

# Create your views here.

class ProjectListView(ListView):
    model = Project
    template_name = "project_list.html"

class ProjectCreateView(CreateView):
    model = Project
    template_name = "project_form.html"
    fields = ['name', 'status', 'location']
    success_url = reverse_lazy('project:project_list')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = "project_form.html"

# class ProjectDelete(DeleteView):
#     model = Project
#     success_url = reverse_lazy('/')
