# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)

from .models import Project, Budget, Entry


# Project views
class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"
    paginate_by = 10

    def get_queryset(self):
        qs = super(ProjectListView, self).get_queryset()

        if self.request.GET.get('name'):
            qs = qs.filter(name__icontains=self.request.GET.get('name'))

        return qs


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'


class ProjectCreateView(SuccessMessageMixin, CreateView):
    model = Project
    template_name = "projects/project_form.html"
    success_message = '%(name)s se agregó correctamente.'
    fields = [
        'name',
        'status',
        'location',
        'project_type',
        'attendant',
        'snip',
        'nog',
        'smip',
        'budget',
        # 'user'
    ]
    success_url = reverse_lazy('projects:project_list')


class ProjectUpdateView(SuccessMessageMixin, UpdateView):
    model = Project
    template_name = "projects/project_form.html"
    success_message = '%(name)s se modificó correctamente.'
    fields = [
        'name',
        'status',
        'location',
        'project_type',
        'attendant',
        'snip',
        'nog',
        'smip',
        'budget',
        # 'user'
    ]
    success_url = reverse_lazy('projects:project_list')


# Budget views
class BudgetListView(ListView):
    model = Budget
    template_name = "projects/budget_list.html"
    context_object_name = "budgets"
    paginate_by = 10


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


# Entrys views
class EntryListView(ListView):
    model = Entry
    template_name = "projects/entry_list.html"
    context_object_name = "entrys"
    paginate_by = 10


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
