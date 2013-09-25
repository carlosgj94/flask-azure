import unittest
from config import config
from resourceprovider import create_app

class AzureSSORouteTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config['testing'])

    def test_post(self):
        raise NotImplementedError

    def tearDown(self):
        raise NotImplementedError