# -*- coding: utf-8 -*-
from math import fsum

from django.shortcuts import render
from django.db.models import Sum
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)

from .models import Project, Budget, Entry
from items.models import Item, File


# Project views
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"
    paginate_by = 10

    def get_queryset(self):
        qs = super(ProjectListView, self).get_queryset()

        if self.request.GET.get('name'):
            qs = qs.filter(name__icontains=self.request.GET.get('name'))

        return qs


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(ProjectDetailView, self).get_context_data(*args, **kwargs)

        ctx['files'] = File.objects.filter(project=self.object)
        if self.object.budget:
            ctx['amount'] = fsum([x.total_cost for x in self.object.budget.entry_set.all()])

        return ctx


class ProjectCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
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
        # 'user'
    ]
    success_url = reverse_lazy('projects:project_list')


class ProjectUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
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
        # 'user'
    ]
    success_url = reverse_lazy('projects:project_list')


# Budget views
class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = "projects/budget_list.html"
    context_object_name = "budgets"
    paginate_by = 10


class BudgetCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    template_name = "projects/budget_form.html"
    fields = [
        "amount",
        "name"
    ]
    success_url = reverse_lazy('projects:budget_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.project = Project.objects.get(
            pk=self.kwargs.get('project_id')
        )
        self.object.save()
        self.success_url = reverse_lazy(
            'projects:project_detail',
            kwargs={
                'pk': self.kwargs.get('project_id')
            }
        )

        return super(BudgetCreateView, self).form_valid(form)


class BudgetUpdateView(LoginRequiredMixin, UpdateView):
    model = Budget
    template_name = "projects/budget_form.html"
    fields = [
        "name",
        "amount",
    ]
    success_url = reverse_lazy('projects:budget_list')

    def get_success_url(self):
        self.success_url = reverse_lazy(
            'projects:project_detail',
            kwargs={
                'pk': self.kwargs.get('project_id')
            }
        )

        return super(BudgetUpdateView, self).get_success_url()


# Entrys views
class EntryListView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = "projects/entry_list.html"
    context_object_name = "entrys"
    paginate_by = 10


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = "projects/entry_form.html"
    fields = [
        "description",
        "quantity",
        "unity",
        "unit_cost",
    ]
    success_url = reverse_lazy('projects:entry_list')

    def get_context_data(self, *args, **kwargs):
        ctx = super(EntryCreateView, self).get_context_data(*args, **kwargs)
        budget = Budget.objects.get(
            pk=self.kwargs.get('budget_id')
        )

        ctx['amount'] = budget.amount - fsum([x.total_cost for x in budget.entry_set.all()])

        return ctx

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.budget = Budget.objects.get(
            pk=self.kwargs.get('budget_id')
        )
        self.object.save()
        self.success_url = reverse_lazy(
            'projects:project_detail',
            kwargs={
                'pk': self.kwargs.get('project_id')
            }
        )

        return super(EntryCreateView, self).form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    template_name = "projects/entry_form.html"
    fields = [
        "description",
        "quantity",
        "unity",
        "unit_cost",
    ]
    success_url = reverse_lazy('projects:entry_list')

    def get_context_data(self, *args, **kwargs):
        ctx = super(EntryUpdateView, self).get_context_data(*args, **kwargs)
        project = Project.objects.get(
            pk=self.kwargs.get('project_id')
        )

        ctx['amount'] = project.budget.amount - fsum([x.total_cost for x in project.budget.entry_set.all()])

        return ctx

    def get_success_url(self):
        self.success_url = reverse_lazy(
            'projects:project_detail',
            kwargs={
                'pk': self.kwargs.get('project_id')
            }
        )

        return super(EntryUpdateView, self).get_success_url()
