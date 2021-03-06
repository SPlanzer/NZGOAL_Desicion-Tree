from django.conf import settings
from django.conf.urls import url, include

from . import views

app_name = 'dtree'

urlpatterns = [
    url(r'^about/$', views.about, name = 'about'),
    url(r'datasets/$|^$', views.datasets, name = 'datasets'),
    url(r'^(?P<dataSet_id>[0-9]+)/$', views.detail, name = 'detail'),
    url(r'^(?P<dataSet_id>[0-9]+)/addldsid/$', views.addLdsId, name = 'addldsid'),
    url(r'^(?P<dataSet_id>[0-9]+)/remove/$', views.removeDataSet, name = 'remove'),
    url(r'^create_dataset/$', views.createDataSet, name='createdataset'),
    url(r'^audit/$', views.audit, name='audit'),
    url(r'yes/$', views.uDecision, name='yes'),
    url(r'no/$', views.uDecision, name='no'),
    url(r'ok/$', views.uDecision, name='ok'),
]
# #ths is to ensure we dont go live with this statis set up
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, dtree=settings.STATIC_ROOT_)