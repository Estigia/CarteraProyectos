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


class ItemCreateView(CreateView):
    model = Item
    fields = [
        "name",
        "attendant",
        "status",
    ]
    template_name = 'items/item_form.html'
    success_url = reverse_lazy('items:item_list')


class ItemListView(ListView):
    model = Item
    template_name = 'items/item_list.html'
    context_object_name = 'items'
