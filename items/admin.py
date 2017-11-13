from django.contrib import admin
from .models import Item, File
from .forms import ItemForm, FileForm


class ItemAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "attendant",
        "create_time",
        "update_time",
    ]
    form = ItemForm


class FileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "file",
        "status",
        "create_time",
        "update_time",
        "project",
        "item",
    ]
    form = FileForm


admin.site.register(Item, ItemAdmin)
admin.site.register(File, FileAdmin)
