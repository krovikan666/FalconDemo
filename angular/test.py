from falcon import HTTP_200
from json import dumps
from mako.template import Template


class TestAngularApp:
    """Test Angular App to display data from test API"""

    test_template = Template(filename='angular/templates/test.mako')

    def on_get(self, request, response):
        """getter for the API call"""

        response.status = HTTP_200
        response.content_type = 'text/html'
        response.body = self.test_template.render()
