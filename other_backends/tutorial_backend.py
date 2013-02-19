from mustachebox.backends import BaseBackend
import random


class Backend(BaseBackend):

    def test_method(self, **kwargs):
        """
          render a simple time serie suitable for javascript graphs :
          [
            {'year':
                [2004, 2005, 2006, 2007]
            },
            {'sale':
                [1000, 1170, 660, 1030]
            },
            {'expenses':
                [400, 460, 1120, 540]
            }
            ]
        """
        self.template = "area"
        resp = {2004: ['2004'],
                2005: ['2005'],
                2006: ['2006'],
                2007: ['2007']}

        for i in range(2):
            for k, v in resp.iteritems():
                    v.append(int((random.random() * random.random()) * 10000))
        resp['label'] = ['year', 'sales', 'expenses']
        return resp
