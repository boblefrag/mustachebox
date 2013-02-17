"""
This set of templatetags are used to show graph in any pages of your project.
"""

from django import template
from django.conf import settings

register = template.Library()

def do_graph_node(parser, token):
    """
    render a GraphNode with the right parameters
    """
    try:
        arguments = token.split_contents()
        method = arguments[1]
        args = arguments[2:]
    except ValueError:
        raise template.TemplateSyntaxError, """
%r tag requires at least 1 argument, the name of the graph you want to render
""".format(token.contents.split()[0])
        
    return GraphNode(method, *args)


class GraphNode(template.Node):
    def __init__(self, method, *args):
        self.method = method
        self.args = args
        backend = __import__(
            "mustachebox.backends.{0}".format(settings.GRAPH_BACKEND),
            fromlist=["Backend"]
            )
        klass = getattr(backend, "Backend")
        self.obj = klass(name=self.method, *self.args)

    def render(self, context):
        print context['STATIC_URL']
        t = template.loader.get_template(
            'mustachebox/tags/{0}.html'.format(self.method)
            )
        print self.obj.name
        return t.render(
            template.Context(
                {'object': self.obj,
                 "STATIC_URL":context['STATIC_URL']},
                 autoescape=context.autoescape)
            )

register.tag('graph', do_graph_node)
