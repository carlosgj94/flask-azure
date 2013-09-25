import unittest
from config import config
import jinja2
from resourceprovider import create_app


class AzureCloudServiceRouteTest(unittest.TestCase):

    def setUp(self):
        self.config = config['testing']
        self.app = create_app(self.config)
        self.url = '%s:%s/subscriptions/%s/cloudservices/%s' % (
            self.config['host'],
            self.config['port'],
            self.config['subscription_id'],
            self.config['cloudservice_id'])
        self.client = self.app.test_client()

    def test_get(self):
        # TODO create subscription and resource necessary for cloud service to exist prior to testing
        # registration_result = self.do_register_subscription()
        # create_result = self.do_create_resource()
        raise NotImplementedError
        # r =  self.client.get(self.url)
        # assert r.status == 200

    def test_delete(self):
        # TODO create subscription and resource necessary for cloud service to exist prior to testing
        # registration_result = self.do_register_subscription()
        # create_result = self.do_create_resource()
        raise NotImplementedError
        # r = self.client.delete(self.url)
        # assert r.status == 200
