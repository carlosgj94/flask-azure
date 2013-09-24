"""
TODO: what is an event?
"""

from base import Model

class Event(Model):
    fields = {
        '_id': str,
        'entity_state': str,
        'subscription_creation_date': str,
        'operation_id': str,
        'resource_type': str,
        'email': str,
        'opt_in': str,
        'subscription_id': str,
        'subscription': str
    }