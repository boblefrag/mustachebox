Tutorial
========

In this tutorial I will show you how to create your own backend and
how to render graph using this backend.

Create the Backend
------------------

The backend file can be located anywhere in your project. For example,
the example backend of mustachebox is located in

::

    mustachebox/backends/example_backend

But this is only an example and you can create your own backend in
your own apps if you prefer.

For this exemple, you can create a file named "tutorial_backend" in
the backends directory of mustachbox applications.

::

    mustachebox/backends/tutorial_backend


Backend Format
______________

The format of the backend you create is realy simple. mustachebox will
look for a class named Backend. This class must inherit
"mustachebox.backends.BaseBackend":

::

    from mustachebox.backends import BaseBackend

    class Backend(BaseBackend):


Define your first method
------------------------

You can write any method you want, doing any work you need but it must
return serializable data. For exemple, you cannot return python
objects or datetime objects.

Your method will be given a kwarg parameter. You can use this
parameter to change the data this method return.

for this tutorial, we will use pre-generated data to generate a time serie. This
time serie will be render as is by the method because mustachebox will
convert it to json befor rendering the template.

::

    def test_method(self, **kwargs):
        """
        render a simple time serie suitable for javascript graphs :
            {
                2004: ['2004', 7160, 546],
                2005: ['2005', 5654, 5435],
                2006: ['2006', 7656, 6545],
                2007: ['2007', 5435, 6545],
                'label': ['year', 'sales', 'expenses']
            }
        """
        response = {
                2004: ['2004', 7160, 546],
                2005: ['2005', 5654, 5435],
                2006: ['2006', 7656, 6545],
                2007: ['2007', 5435, 6545],
                'label': ['year', 'sales', 'expenses']
            }
        return response


You can now test the method in the shell ::

    python manage.py shell
    >>> from mustachebox.backends.tutorial_backend import Backend
    >>> Backend(name="test_method").data
    '{2004: ['2004', 7160, 546], 2005: ['2005', 5654, 5435], 2006:
    ['2006', 7656, 6545], 2007: ['2007', 5435, 6545], 'label': ['year', 'sales', 'expenses']}'


Rendering
---------

In order to render your graph, you must define a template. This can be
done in your method. For this tutorial we will use the pre-existing
area template. This template is suitable for rendering area graphs. So
add this at the begining of your method

::

    self.template = "area"

Testing
_______

You can now easily test your new method. Just change the backend in
your settings :

::

    GRAPH_BACKEND="mustachebox.backends.tutorial_backend"

and hit your graph url:

(http://localhost:8000/graphs/test_method/)

Add the templatetag
-------------------

Your graph can already be rendered as a templatetag. Anywhere in your
application you can write :

::

    {% load graph %}
    {% graph test_method %}

This is because you use the area template and this template exist in
the form of a complete template and in the form of a templatetag
template.

Getting the json
________________

Of course you can retreive the json form of your data. For this you
can write anywhere in your application an ajax call tu your url :

::

    $.ajax({
        type:"GET",
        url: 'http://localhost:8000/graphs/test_method/',
        success: function(response){
            do_something_with_response(response)
        }
    })
