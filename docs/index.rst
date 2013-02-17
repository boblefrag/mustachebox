.. mustachebox documentation master file, created by
   sphinx-quickstart on Sun Feb 17 15:51:46 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to mustachebox's documentation!
=======================================

Contents:

.. toctree::
   :maxdepth: 2

   installation
   quickstart
   backends
   templatetags
   json_data


Description
-----------

Mustache Box is a set of utilities to help you presenting graph of various data in a Django Project. Data can come from whatever source you want :

    * Distant API
    * Couchdb databases
    * Your Django models
    * ...

3 parts architecture :
______________________

To make a graph you will need 3 parts :

    * a method : the method lie in a Backend you create (or you can
      use predefine ones). Each method is responsible for gathering
      data (the way you want) and parse it to give a formated version
      of the data to the template.

    * A template: the template is a classic HTML file made to hold
      your graph. You can use some predefine template or use your
      custom one

    * a javascript file : the javascript file take your data and
      render a graph using the external dependencies you need (jquery,
      d3js, raphaël, etc...)

Features
--------

Of course there is serval features you gain with this architecture :

    * url auto-discovering : You do not have to design an url for each
      method. Mustache Box take the pain away for you and design urls
      for you. Of course, if you don't like this feature, you can
      design your own urls for each graphs.

    * request/ajax response : each url responds either to classic
      request ( rendering a template with the data ) and to ajax
      returning only the formated json suitable for javasccript
      call. It has never be so easy to create long-pooling call.

    * reusability: mustachebow is made in a reusable fashion. You can
      mix together your methods, javasccript files and html to present
      different data with the same template and/or javascript, or
      present the same data in different manners easily

    * templatetags: when you create a graph you can use it in a
      templatetag too. It's really easy to do. You just have to write
      another template to hold your graph in the templatetag.


This software is released under GPLv3

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

