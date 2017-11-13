from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)

from .models import Item, File
from projects.models import Project


class ItemCreateView(CreateView):
    model = Item
    fields = [
        "name",
        "attendant",
    ]
    template_name = 'items/item_form.html'
    success_url = reverse_lazy('items:item_list')


class ItemListView(ListView):
    model = Item
    template_name = 'items/item_list.html'
    context_object_name = 'items'


class FileCreateView(CreateView):
    model = File
    template_name = 'items/file_form.html'
    success_url = reverse_lazy('projects:project_list')
    fields = [
        'file',
        'status',
        'item'
    ]

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

        return super(FileCreateView, self).form_valid(form)


class FileUpdateView(UpdateView):
    model = File
    template_name = 'items/file_form.html'
    fields = [
        'file',
        'status',
        'item'
    ]

    def get_success_url(self):
        self.success_url = reverse_lazy(
            'projects:project_detail',
            kwargs={
                'pk': self.kwargs.get('project_id')
            }
        )

        return super(FileUpdateView, self).get_success_url()
