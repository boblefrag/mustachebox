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

from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from views import GraphDetailView, GraphListView

urlpatterns = patterns(
    '',
    url(r'^all/$', GraphListView.as_view()),
    url(r'^template_tag_test/$', TemplateView.as_view(
        template_name="mustachebox/templatetags_test.html")),
    url(r'^(?P<name>[-_\w]+)/$',
        GraphDetailView.as_view(),
        name="graph"
        ),
)
