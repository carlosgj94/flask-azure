"""
TODO: what is a Subscription?
"""

from base import Model

class Subscription(Model):
    fields = {
        '_id': str,
        'created_date': str,
        'state': str
    }