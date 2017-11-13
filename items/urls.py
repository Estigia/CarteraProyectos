from django.conf.urls import url
from .views import (
    ItemCreateView,
    ItemListView,
    FileCreateView,
    FileUpdateView,
    FileDetailView,
    ItemUpdateView
)

urlpatterns = [
    url(r'^new/$', ItemCreateView.as_view(), name='item_new'),
    url(r'^$', ItemListView.as_view(), name='item_list'),
    url(r'^(?P<pk>[\w|\d|-]+)/edit/$', ItemUpdateView.as_view(), name="item_edit"),
    url(r'^(?P<project_id>[\w|\d|-]+)/file/new/$', FileCreateView.as_view(), name="file_new"),
    url(r'^(?P<project_id>[\w|\d|-]+)/file/(?P<pk>[\w|\d|-]+)/edit/$', FileUpdateView.as_view(), name='file_edit'),
    url(r'^(?P<project_id>[\w|\d|-]+)/file/(?P<pk>[\w|\d|-]+)/$', FileDetailView.as_view(), name='file_detail')
]
