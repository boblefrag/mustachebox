from django.conf.urls import patterns, url
from views import GraphDetailView

urlpatterns = patterns(
    '',
#    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<slug>[-_\w]+)/$',
        GraphDetailView.as_view(),
        {'client': "onqrsq8KYlRH9Yg3BC22Vg",
         'secret': "Fkfo0tiajGcQzqKlBm5jX3d6UkTOsBsAOLE6MtSZDxs"},
        name="graph"
        )
)
