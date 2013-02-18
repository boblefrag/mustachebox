Installation
============

Requirements
------------

mustache box has no particular dependencies. As a django-app it need a
working version of Django >= 1.3.

But in order to use the example backend, particulary the page listing
all the graphs you can use, you have to install the docutils.

so just clone this repository :

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

    GRAPH_BACKEND="mustachebox.backends.example_backend"

Add the mustachebox urls to your project
________________________________________

include mustachbox to your urls :

::

    url(r'^graphs/', include('mustachebox.urls')),

Testing
-------

To start playing with MustacheBox, you can visit :

(http://localhost:8000/grapher/all/)

That list all the graphs the example backend can give you.
