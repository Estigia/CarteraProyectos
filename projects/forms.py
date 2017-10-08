from django import forms

from .models import (Project, Bugdet, Entry)

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
            "create_time",
            "update_time",
            "Budget_id",
            "User_id",
        ]

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = [
            "amount",
            "create_time",
            "update_time",
        ]


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [
            "description",
            "quantity",
            "unity",
            "unit_cost",
            "create_time",
            "update_time",
            "Budget_id",
        ]
