from . import views

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib import admin
from person.views import PersonViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'person', PersonViewSet, base_name='person')


urlpatterns = (
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^person/(?P<id>\d+)/$', views.detail),
    # url(r'^add/$', views.add_or_edit, {'id': None}),
    # url(r'^edit/(?P<id>\d+)/$', views.add_or_edit),
    url(r'^delete/(?P<id>\d+)/$', views.delete),
    # url(r'^$', views.index),
    url(r'^get_all_persons/$', views.get_all_persons),

)