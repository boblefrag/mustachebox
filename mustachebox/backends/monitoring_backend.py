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
        resp['label'] = ['year','sales', 'expenses']
    return resp



class Backend(BaseBackend):
    """
    A backend get data formated as mustache need them.
    - data : contain the data to be printed as graph
    - name : the graph name
    - template_name: the template to use for rendering
    """

    def monitoring(self, **kwargs):
        """
        Return a set of data to be represented as a graph
        """
        records = []
        for i in range(10):
            # 1 instances
            instance = Instance(i)
            date = datetime.datetime(2012, 1, 1, 0, 0, 0)
            for i in range(300):
                # this dataset consist of 300 metrics for 10 machines
                date += datetime.timedelta(minutes=65)
                record = Record(instance.name, date)

                records.append(
                    {'instance': instance.name,
                     'cpu': record.CPU,
                     'ram': record.RAM,
                     'La1': record.La1,
                     'La2': record.La2,
                     'La3': record.La3,
                     'date': record.date
                     }
                    )
        self.template = "crossfilter"
        return records

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

        return {'label' : label, 'activities': activities}


        

class Record(object):
    """
    Metric about an instance.
    CPU, RAM, Load Average 1 sec 5 sec and 1 minute.
    """
    def __init__(self, instance, date):
        """ instance is just a name to identify a set of data """
        self.instance = instance
        self.CPU  = random.random() * 100
        self.RAM  = random.random() * 100
        self.La1 = random.random() * 10
        self.La2 = random.random() * 10
        self.La3 = random.random() * 10
        self.date = time.mktime(date.timetuple())



class Instance(object):
    """
    An instance to identify metrics.
    Each metric are attached to an instance
    """
    def __init__(self, name):
        self.name = "instance_%i" % name

        
