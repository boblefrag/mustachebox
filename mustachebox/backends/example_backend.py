import json
import datetime
import time
import random
from mustachebox.backends import BaseBackend


def time_serie(**kwargs):
    """
    Render a time serie
    """
    resp = {2004: ['2004'],
            2005: ['2005'],
            2006: ['2006'],
            2007: ['2007']}

    for i in range(2):
        for k, v in resp.iteritems():
            v.append(int((random.random() * random.random()) * 10000))
        resp['label'] = ['year', 'sales', 'expenses']
    return resp


class Backend(BaseBackend):
    """
    A backend get data formated as mustache need them.
    - data : contain the data to be printed as graph
    - name : the graph name
    - template_name: the template to use for rendering
    """

    def area(self, **kwargs):
        self.template = 'area'
        return time_serie(**kwargs)

    def bar_chart(self, **kwargs):
        self.template = "barchart"
        return time_serie(**kwargs)

    def column_chart(self, **kwargs):
        self.template = 'columnchart'
        return time_serie(**kwargs)

    def pie_chart(self):
        """
        define a generic pie chart
        """
        self.template = "pie_chart"

        label = ['name', 'count']
        activities = []
        words = ['eat', 'read', 'work', 'sleep', 'watch TV']
        for elem in words:
            activities.append([elem, int(random.random() * 10)])

        return {'label': label, 'activities': activities}

    def line_chart(self):
        """
        define a generic line chart
        response is a list of dict :
        [
          {'date': 1107151200000,
           'value': 289
           },
          {'date': 1109743200000,
           'value': 766
           }
           ...
        ]
        """
        response = []
        self.template = "line_chart"
        date = datetime.datetime(2005, 1, 1, 0, 0, 0)
        for i in range(1500):
            date += datetime.timedelta(days=2)
            response.append({
                'date': time.mktime(date.timetuple()) * 1000,
                'value': (i * 10) + int(random.random() * 1000)})
        return response
