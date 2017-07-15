from . import views

urlpatterns = (
    (r'^person/(?P<id>\d+)/$', 'demoProject2.person.views.detail'),
    (r'^add/$', 'demoProject2.person.views.add_or_edit', {'id': None}),
    (r'^edit/(?P<id>\d+)/$', 'demoProject2.person.views.add_or_edit'),
    (r'^delete/(?P<id>\d+)/$', 'demoProject2.person.views.delete'),
    (r'^$', 'demoProject2.person.views.index'),
)