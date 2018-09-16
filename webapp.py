import falcon
from angular.test import TestAngularApp
from api.test import TestJSON

app = falcon.API()

# Setup test API
test = TestJSON()
app.add_route('/api/test', test)

# Setup test App
test_app = TestAngularApp()
app.add_route('/test', test_app)
