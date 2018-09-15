import falcon
from api.test import TestJSON

app = falcon.API()

# Setup test API
test = TestJSON()
app.add_route('/test', test)
