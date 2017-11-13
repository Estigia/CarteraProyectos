from django import forms
from .models import Item, File


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "name",
            "attendant",
        ]


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = [
            "file",
            "item",
            "status",
            "project"
        ]
