from django.conf.urls import *
from . import view, testdb
from . import view, search
from . import view, search2

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^query', testdb.query),
    url(r'^update', testdb.update),
    url(r'^delete', testdb.delete),
    url(r'^search-form$',search.search_form),
    url(r'^search$',search.search),
    url(r'^search-post$', search2.search_post),
]