import unittest
from config import config
from helpers import make_resource
from resourceprovider import create_app


class AzureResourceRouteTest(unittest.TestCase):

    def setUp(self):
        base_url = '{base_uri}/subscriptions/{subscription_id}/cloudservices/{cloud_service_name}/resources/{resource_type}/{resource_name}'
        self.config = config['testing']
        self.app = create_app(self.config['app'])
        self.url = base_url.format(**self.config['resource']['url'])
        self.client = self.app.test_client()
        self.resource = make_resource(self.client, self.url, self.config['resource']['doc'])

    def test_get(self):
        # create resource
        self.resource('put')
        # retrieve resource
        r = self.resource('get')
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
