Installation
============

Requirements
------------

mustache box has no particular dependencies. As a django-app it need a
working version of Django >= 1.3 so just clone this repository : 

Cloning the repository
----------------------

::

    hg clone https://boblefrag@bitbucket.org/boblefrag/mustachebox

Install Steps
-------------

Adding the app to the INSTALLED_APPS
____________________________________
::

    # settings.py

     INSTALLED_APPS = (
    ...
    'mustachebox',
    )


Defining a GRAPH_BACKEND
________________________

As mustachebox rely on a backend, you must define your own. It's realy
easy however. For a starting point, you can use the
monitor_backend. This backend exist for testing and example purpose.

::

    GRAPH_BACKEND="monitoring_backend"

Add the mustachebox urls to your project
________________________________________

include mustachbox to your urls :

::

    url(r'^graphs/', include('mustachebox.urls')),

Testing
-------

To validate that everything is correctly installed you can use those
urls :

For testing the main views :

- http://localhost:8000/graphs/monitoring/

For testing the templatetag system :

- http://localhost:8000/grapher/template_tag_test/

This is the same graph but rendered using a templatetags instead of
the view.
