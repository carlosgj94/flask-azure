"""
TODO: what is a CloudService?
"""

from base import Model

class CloudService(Model):
    fields = {
        '_id': str,
        'name': str,
        'geo_region': str,
        'subscription_id': str,
        'subscription': str
    }