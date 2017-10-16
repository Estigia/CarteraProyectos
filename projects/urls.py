from django.conf.urls import url

from .views import (
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
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
    # Budget urls
    url(r'^budget/$', BudgetListView.as_view(), name='budget_list'),
    url(r'^budget/new/$', BudgetCreateView.as_view(), name='budget_new'),
    url(r'^budget/edit/(?P<pk>[\w|\d|-]+)/$', BudgetUpdateView.as_view(), name='budget_edit'),
    # Entry urls
    url(r'^entry/$', EntryListView.as_view(), name='entry_list'),
    url(r'^entry/new/$', EntryCreateView.as_view(), name='entry_new'),
    url(r'^entry/edit/(?P<pk>[\w|\d|-]+)/$', EntryUpdateView.as_view(), name='entry_edit'),
]
