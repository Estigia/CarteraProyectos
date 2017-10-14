from django.shortcuts import render

from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Project, Budget, Entry

#Prject views

class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"

class ProjectCreateView(CreateView):
    model = Project
    template_name = "projects/project_form.html"
    fields = [
        'name',
        'status',
        'location'
    ]
    success_url = reverse_lazy('projects:project_list')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = "projects/project_form.html"
    fields = [
        'name',
        'status',
        'location'
    ]
    success_url = reverse_lazy('projects:project_list')

#Budget views

class BudgetListView(ListView):
    model = Budget
    template_name = "projects/budget_list.html"
    context_object_name = "budgets"


class BudgetCreateView(CreateView):
    model = Budget
    template_name = "projects/budget_form.html"
    fields = [
        "amount",
    ]
    success_url = reverse_lazy('projects:budget_list')

class BudgetUpdateView(UpdateView):
    model = Budget
    template_name = "projects/budget_form.html"
    fields = [
        "amount",
    ]
    success_url = reverse_lazy('projects:budget_list')

#Entrys views

class EntryListView(ListView):
    model = Entry
    template_name = "projects/entry_list.html"
    context_object_name = "entrys"

class EntryCreateView(CreateView):
    model = Entry
    template_name = "projects/entry_form.html"
    fields = [
        "description",
        "quantity",
        "unity",
        "unit_cost",
    ]
    success_url = reverse_lazy('projects:entry_list')

class EntryUpdateView(UpdateView):
    model = Entry
    template_name = "projects/entry_form.html"
    fields = [
        "description",
        "quantity",
        "unity",
        "unit_cost",
    ]
    success_url = reverse_lazy('projects:entry_list')
