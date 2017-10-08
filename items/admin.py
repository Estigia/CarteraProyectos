from django.contrib import admin
from .models import Item, File
from .forms import ItemForm, FileForm


class ItemAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "attendant",
        "status",
        # "project",
        # "budget",
        "create_time",
        "update_time",
    ]
    form = ItemForm

class FileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "file",
        "create_time",
        "item",
    ]
    form = FileForm


admin.site.register(Item, ItemAdmin)
admin.site.register(File, FileAdmin)
