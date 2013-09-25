"""
Helper functions for achieving state in tests.
"""

import jinja2

def make_template(self, template_path, config):
    with open(template_path, 'r') as f:
        template = jinja2.Template(f.read())
    return template

def make_resource(client, url, config):
    template = make_template('tests/templates/resource.xml')
    def resource(method):
        data = template.render(**config)
        return getattr(client, method)(url, data=data)
    return resource

def make_subscribe(client, url):
    template = make_template('tests/templates/subscription.xml')
    def subscribe(state, config):
        config.update({'state': state})
        data = template.render(**config)
        return client.post(url, data=data)
    return subscribe