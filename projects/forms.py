from django import forms

from .models import (Project, Budget, Entry)

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = [
        "amount",
        ]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "status",
            "location",
            "project_type",
            "attendant",
            "snip",
            "nog",
            "smip",
            "budget",
            # "user",
        ]

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [
            "description",
            "quantity",
            "unity",
            "unit_cost",
            "budget",
        ]
