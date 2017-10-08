from django.conf.urls import url
from .views import (
    ItemCreateView,
    ItemListView,
)

urlpatterns = [
    url(r'^new/', ItemCreateView.as_view(), name='item_new'),
    url(r'^', ItemListView.as_view(), name='item_list'),
]
