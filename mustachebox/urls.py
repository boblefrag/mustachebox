from django.conf.urls import patterns, url
from views import GraphDetailView

urlpatterns = patterns(
    '',
#    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<name>[-_\w]+)/$',
        GraphDetailView.as_view(),
        name="graph"
        )
)
