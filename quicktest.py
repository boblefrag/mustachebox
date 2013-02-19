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


import os
import sys
import argparse
from django.conf import settings

class QuickDjangoTest(object):
    """
    A quick way to run the Django test suite without a fully-configured project.

    Example usage:

        >>> QuickDjangoTest('app1', 'app2')

    Based on a script published by Lukasz Dziedzia at:
    http://stackoverflow.com/questions/3841725/how-to-launch-tests-for-django-reusable-app
    """
    DIRNAME = os.path.dirname(__file__)
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django_coverage'
    )

    def __init__(self, *args, **kwargs):
        self.apps = args
        # Get the version of the test suite
        self.version = self.get_test_version()
        # Call the appropriate one
        if self.version == 'new':
            self._new_tests()
        else:
            self._old_tests()

    def get_test_version(self):
        """
        Figure out which version of Django's test suite we have to play with.
        """
        from django import VERSION
        if VERSION[0] == 1 and VERSION[1] >= 2:
            return 'new'
        else:
            return 'old'

    def _old_tests(self):
        """
        Fire up the Django test suite from before version 1.2
        """
        settings.configure(DEBUG = True,
           DATABASE_ENGINE = 'sqlite3',
           DATABASE_NAME = os.path.join(self.DIRNAME, 'database.db'),
           INSTALLED_APPS = self.INSTALLED_APPS + self.apps,
           ROOT_URLCONF = 'grapher.urls'
        )
        from django.test.simple import run_tests
        failures = run_tests(self.apps, verbosity=1)
        if failures:
            sys.exit(failures)

    def _new_tests(self):
        """
        Fire up the Django test suite developed for version 1.2
        """
        settings.configure(
            DEBUG = True,
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(self.DIRNAME, 'database.db'),
                    'USER': '',
                    'PASSWORD': '',
                    'HOST': '',
                    'PORT': '',
                }
            },
            INSTALLED_APPS = self.INSTALLED_APPS + self.apps,
            ROOT_URLCONF = 'test_urls',
            GRAPH_BACKEND="mustachebox.backends.example_backend"
        )


        from django_coverage.coverage_runner import CoverageRunner
        failures = CoverageRunner().run_tests(self.apps, verbosity=1)
        if failures:
            sys.exit(failures)

if __name__ == '__main__':
    """
    What do when the user hits this file from the shell.

    Example usage:

        $ python quicktest.py app1 app2

    """
    parser = argparse.ArgumentParser(
        usage="[args]",
        description="Run Django tests on the provided applications."
    )
    parser.add_argument('apps', nargs='+', type=str)
    args = parser.parse_args()
    QuickDjangoTest(*args.apps)
