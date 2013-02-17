import json
import datetime
import time
import random
from mustachebox.backends import BaseBackend

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
