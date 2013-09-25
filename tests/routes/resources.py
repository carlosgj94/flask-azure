import unittest
from config import config
from resourceprovider import create_app

class AzureResourceRouteTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config['testing'])
        self.url = '/subscriptions/%s/cloudservices/%s/resources/%s/%s' % (
            self.config['subscription_id'],
            self.config['cloud_service_name'],
            self.config['resource_type'],
            self.config['resource_name'])
        self.client = self.app.test_client()
        with open('tests/templates/resource.xml', 'r') as f:
            self.template = jinja2.Template(f.read())

    def template_body(self):
        return self.template.render(**self.config)

    def resource(self, method):
        return getattr(self.client, method)(self.url, data=self.template_body())

    def test_get(self):
        # create resource
        resource('put')
        # retrieve resource
        r = resource('get')
        assert r.status == 200

    def test_put(self):
        # create resource
        r = resource('put')
        assert r.status == 200

    def test_post(self):
        # create resource
        resource('put')
        # upgrade resource
        r = resource('post')
        assert r.status == 200

    def test_delete(self):
        # create resource
        resource('put')
        # delete resource
        r = resource('delete')
        assert r.status == 200

    def tearDown(self):
        pass