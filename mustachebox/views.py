from django.views.generic.detail import DetailView
from django.conf import settings
from django import http

class GraphDetailView(DetailView):
    """
    This class represent a graph data.
    The data you will use to represent a graph may not be part of you application
    nor your project. It can be somethin' commin' from an external API, a nosql backend, 
    your cache backend and so one.

    So GraphDetailView implement a "get object" method to retreive the data using the backend you have define
    in your settings.

    Look at mustachebox.backends for an example backend
    """
    def get_object(self):
        backend = __import__(
            settings.GRAPH_BACKEND,
            fromlist=["Backend"]
            )
        klass = getattr(backend, "Backend")
        obj = klass(**self.kwargs)
        

        return obj
    
    def get_context_object_name(self,obj):
        return "object"

    def get_template_names(self):
        return "mustachebox/{0}.html".format(self.object.template)

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            return http.HttpResponse(context['object'].data,
                                 content_type='application/json',
                                 **response_kwargs)
        return super(GraphDetailView, self).render_to_response(context, **response_kwargs)
