"""
Base model subsequent models inherit from
"""

class Model(object):
    # {fieldname: validator_function}
    fields = {}

    def __init__(self, **kwargs):
        # make sure each needed field passes snuff
        for field, validator in fields:
            try:
                validator(kwargs.get(field))
            except Exception as e:
                raise e
            else:
                # assign to self accordingly
                setattr(self, field, kwargs.get(field))

    def save(self):
        raise NotImplementedError

    def get(self, id):
        raise NotImplementedError