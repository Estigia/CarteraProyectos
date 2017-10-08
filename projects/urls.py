from django.conf.urls import url

from .views import (
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView
)

urlpatterns = [
    url(r'^$', ProjectListView.as_view(), name='project_list'),
    url(r'^new/$', ProjectCreateView.as_view(), name='project_new'),
    url(r'^edit/(?P<pk>\d+)$', ProjectUpdateView.as_view(), name='project_edit'),
]
