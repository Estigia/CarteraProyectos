from django.conf.urls import url

from .views import (
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDetailView,
    BudgetListView,
    BudgetCreateView,
    BudgetUpdateView,
    EntryListView,
    EntryCreateView,
    EntryUpdateView,
)

urlpatterns = [
    # Project urls
    url(r'^$', ProjectListView.as_view(), name='project_list'),
    url(r'^new/$', ProjectCreateView.as_view(), name='project_new'),
    url(r'^edit/(?P<pk>[\w|\d|-]+)/$', ProjectUpdateView.as_view(), name='project_edit'),
    url(r'^detail/(?P<pk>[\w|\d|-]+)/$', ProjectDetailView.as_view(), name='project_detail'),
    # Budget urls
    url(r'^budget/$', BudgetListView.as_view(), name='budget_list'),
    url(r'^(?P<project_id>[\w|\d|-]+)/budget/new/$', BudgetCreateView.as_view(), name='budget_new'),
    url(r'^(?P<project_id>[\w|\d|-]+)/budget/edit/(?P<pk>[\w|\d|-]+)/$', BudgetUpdateView.as_view(), name='budget_edit'),
    # Entry urls
    url(r'^entry/$', EntryListView.as_view(), name='entry_list'),
    url(r'^(?P<project_id>[\w|\d|-]+)/budget/(?P<budget_id>[\w|\d|-]+)/entry/new/$', EntryCreateView.as_view(), name='entry_new'),
    url(r'^(?P<project_id>[\w|\d|-]+)/entry/edit/(?P<pk>[\w|\d|-]+)/$', EntryUpdateView.as_view(), name='entry_edit'),
]
