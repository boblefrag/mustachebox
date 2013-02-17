from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from views import GraphDetailView

urlpatterns = patterns(
    '',
#    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^template_tag_test/$', TemplateView.as_view(
        template_name="mustachebox/templatetags_test.html")),
        
    url(r'^(?P<name>[-_\w]+)/$',
        GraphDetailView.as_view(),
        name="graph"
        ),
)
