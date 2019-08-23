from django.conf.urls import *
from . import view, testdb

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^query', testdb.query),
    url(r'^update', testdb.update),
    url(r'^delete', testdb.delete),
    url(r'^search-form$',search.search_form)
]