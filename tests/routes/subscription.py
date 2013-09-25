import unittest
from config import config
import jinja2
from resourceprovider import create_app

class AzureSubscriptionRouteTest(unittest.TestCase):
    def setUp(self):
        self.config = config['testing']
        self.app = create_app(self.config)
        self.url = '%s:%s/subscriptions/%s/Events' % (
            self.config['host'], 
            self.config['port'], 
            self.config['subscription_id'])
        self.client = self.app.test_client()
        with open('tests/templates/subscribe.xml', 'r') as f:
            self.template = jinja2.Template(f.read())

    ### HELPERS

    def template_body(self, state):
        options = {
            'state': state
        }
        options.update(self.config)
        return self.template.render(**options)

    def subscribe(self, state):
        data = self.template_body(state)
        return self.client.post(url, data=data)

    ### TESTS

    def test_register(self):
        r = subscribe('Registered')
        assert r.status == 200

    def test_enable(self):
        # create subscription
        subscribe('Registered')
        # enable subscription
        r = subscribe('Enabled')
        assert r.status == 200

    def test_disable(self):
        # create subscription
        subscribe('Registered')
        # disable subscription
        r = subscribe('Disabled')
        assert r.status == 200

    def test_delete(self):
        # create subscription
        subscribe('Registered')
        # delete subscription
        r = subscribe('Deleted')
        assert r.status == 200

    def tearDown(self):
        pass