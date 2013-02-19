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

import json


class BaseBackend(object):
    """
    BaseBackend must subclassed by custom backends to be used. It only
    define basic utilities to help writing backends
    """

    def __init__(self, **kwargs):
        self.template = None
        self.name = kwargs.pop('name')
        self.data = json.dumps(self.fetch(self.name, **kwargs))

    def fetch(self, method, **kwargs):
        """
        Return a set of data formated information
        """
        meth = getattr(self, method, **kwargs)
        return meth()
