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
    # (r'^person/(?P<id>\d+)/$', 'demoProject2.person.views.detail'),
    # (r'^add/$', 'demoProject2.person.views.add_or_edit', {'id': None}),
    # (r'^edit/(?P<id>\d+)/$', 'demoProject2.person.views.add_or_edit'),
    # (r'^delete/(?P<id>\d+)/$', 'demoProject2.person.views.delete'),
    # (r'^$', 'demoProject2.person.views.index1'),

)