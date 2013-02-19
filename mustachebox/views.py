# -*- coding: utf-8 -*-
# Copyright (c) 2013 Yohann Gabory <yohann@gabory.fr>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.conf import settings
from django import http


class GraphListView(ListView):
    """
    This class return all the avalaible graphs in the current backend
    """
    template_name = "mustachebox/all_graph.html"

    def get_queryset(self):
        """
        This method does not return a queryset because there is no
        database in this app.
        But it return a list of avalaible grapg to be displayed.
        """
        backend = __import__(
            settings.GRAPH_BACKEND,
            fromlist=["Backend"])

        klass = getattr(backend, "Backend")
        responses = []
        for k, v in klass.__dict__.iteritems():
            if hasattr(v, '__call__'):
                responses.append({'name': k, 'doc': v.__doc__})
        return responses


class GraphDetailView(DetailView):
    """
    This class represent a graph data.  The data you will use to
    represent a graph may not be part of you application nor your
    project. It can be somethin' commin' from an external API, a nosql
    backend, your cache backend and so one.

    So GraphDetailView implement a "get object" method to retreive the
    data using the backend you have define in your settings.

    Look at mustachebox.backends for an example backend
    """

    def get_object(self):
        backend = __import__(
            settings.GRAPH_BACKEND,
            fromlist=["Backend"])
        klass = getattr(backend, "Backend")
        try:
            obj = klass(**self.kwargs)
        except AttributeError:
            raise http.Http404
        return obj

    def get_context_object_name(self, obj):
        return "object"

    def get_template_names(self):
        return "mustachebox/{0}.html".format(self.object.template)

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            return http.HttpResponse(context['object'].data,
                                     content_type='application/json',
                                     **response_kwargs)
        return super(
            GraphDetailView, self).render_to_response(
                context,
                **response_kwargs)
