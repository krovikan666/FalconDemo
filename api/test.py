from falcon import HTTP_200
from json import dumps


class TestJSON:
    """Test API call, that returns a JSON """

    data_dict = {
        'data': 'Test data'
    }

    def on_get(self, request, response):
        """getter for the API call"""

        if len(request.params) > 0:
            self.data_dict['params'] = request.params

        response.status = HTTP_200
        response.body = dumps(self.data_dict)
