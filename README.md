#  MustacheBox

[mustache box on wikipedia](http://fr.wikipedia.org/wiki/Bo%C3%AEte_%C3%A0_moustaches)

## Description

Mustache Box is a set of utilities to help you presenting graph of
various data in a Django Project. Data can come from whatever source you want :

* Distant API
* Couchdb databases
* Your Django models
* ...

### A graph consist of 3 parts :

* a method : the method lie in a Backend you create (or you can use
  predefine ones). Each method is responsible for gathering data (the
  way you want) and parse it to give a formated version of the data to
  the template.

* A template: the template is a classic HTML file made to hold your
graph. You can use some predefine template or use your custom one

* a javascript file : the javascript file take your data and render a
  graph using the external dependencies you need (jquery, d3js, raphaël, etc...)

### Features

Of course there is serval features you gain with this architecture :

* url auto-discovering : You do not have to design an url for each
  method. Mustache Box take the pain away for you and design urls for
  you. Of course, if you don't like this feature, you can design your
  own urls for each graphs.

* request/ajax response : each url responds either to classic request
  ( rendering a template with the data ) and to ajax returning only
  the formated json suitable for javasccript call. It has never be so
  easy to create long-pooling call.

* reusability: mustachebow is made in a reusable fashion. You can mix
  together your methods, javasccript files and html to present
  different data with the same template and/or javascript, or present
  the same data in different manners easily

## Installation

mustache box has no particular dependencies.
As a django-app it need a working version of Django >= 1.3
so just clone this repository :

### Clone

    hg clone https://boblefrag@bitbucket.org/boblefrag/mustachebox

### Add to the installed apps

and add mustachebox to the list of your installed apps :

    # settings.py

    INSTALLED_APPS = (
    ...
    'mustachebox',
    )

### define a GRAPH_BACKEND

As mustachebox rely on a backend, you must define your own. It's realy
easy however. For a starting point, you can use the
monitor_backend. This backend exist for testing and example purpose.

    GRAPH_BACKEND="monitoring_backend"

### include mustachbox to your urls :

    url(r'^graphs/', include('mustachebox.urls')),

### Enjoy:

To start playing with mustachebox, you can visit :

(http://localhost:8000/graphs/monitoring/)

This software is released under [GPLv3](http://www.gnu.org/licenses/gpl.html)

