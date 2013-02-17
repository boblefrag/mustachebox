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
        response = {'year':[2004, 2005, 2006, 2007],'sales': [], 'expenses': []}
        for i in range(4):
            response['sales'].append(
                int((random.random() * random.random()) * 10000))
            response['expenses'].append(
                int((random.random() * random.random()) * 10000))
        return response
