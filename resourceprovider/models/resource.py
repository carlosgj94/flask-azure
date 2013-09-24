"""
TODO: what is a Resource?
"""

from base import Model

class Resource(Model):
    fields = {
        '_id': str,
        'name': str,
        'cloudservice_id': str,
        'cloudservice': str,
        'resource_type': str,
        'incarnation_id': str,
        'schema_version': str,
        'plan': str,
        'version': str,
        'intrinsic_settings': str,
        'promotion_code': str,
        'state': str,
        'sub_state': str,
        'output_items': str,
        'usage_meters': str
    }