from django.conf.urls import url
import operator

from .import views
from django.db.models import Q



apps_name = 'library'

urlpatterns =\
    [
    #/library/
    url(r'^$', views.index, name = 'index'),


    url(r'^library/staff/$', views.staff, name = 'staff'),
   # url(r'^library/AllBooks/$', views.Books, name = 'AllBooK'),
    url(r'^library/reader/$', views.reader, name = 'reader'),
        # this url is the same user request "url - mainpage's url like music"
    #url(r'^library/reader/library/reader211/$', views.reader211, name = 'reader211'),
    url(r'^library/reader/library/reader2111/$', views.reader2111, name = 'reader2111'),
    url(r'^library/reader/library/reader211/library/reader2111/$',
        views.reader2111, name='reader2111'),

    url(r'^library/library/reader/library/reader211/library/reader2112/$',
        views.reader2112, name='reader2112'),

    url(r'^library/reader/library/reader212/$', views.reader212, name = 'reader212'),
    url(r'^library/reader/library/reader212/library/reader2112/$',
        views.reader2112, name='reader2112'),
    url(r'^library/reader/library/reader212/library/reader2111/$',
        views.reader2111, name='reader2111'),
    url(r'^library/reader/library/reader212/library/reader2121/$',
        views.reader2121, name='reader2121'),

    url(r'^library/staff/library/reader222/library/UpdateDocument/$',
        views.UpdateDocument, name='UpdateDocument'),

    url(r'^library/staff/library/reader222/$',
        views.reader222, name='reader222'),
    url(r'^library/staff/$',
        views.staff, name='staff'),


    url(r'^library/staff/library/reader222/library/UpdateDocument/library/successfullyinsert/$',
        views.successfullyinsert, name='successfullyinsert'),
]
