from django.contrib import admin

# Register your models here.

from .models import (Project, Budget, Entry)

from .forms import (ProjectForm, BudgetForm, EntryForm)


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "id",
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
    form = ProjectForm

class BudgetAdmin(Admin.ModelAdmin):
    list_display = [
        "id",
        "amount",
        "create_time",
        "update_time",
    ]
    form = BudgetForm

class EntryAdmin(Admin.ModelAdmin):
    list_display = [
        "id",
        "description",
        "quantity",
        "unity",
        "unit_cost",
        "create_time",
        "update_time",
        "Budget_id",
    ]
    form = EntryForm

admin.site.register(Project, ProjectAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Entry, EntryAdmin)
