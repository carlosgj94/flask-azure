import flask
import flask.views
from flask import request
from resourceprovider.util import xml_dict
from resourceprovider.controllers import resources as ctrl

resources = flask.Blueprint('resources', __name__)
url = '/subscriptions/<subscription_id>/cloudservices/<cloud_service_name>/resources/<resource_type>/<resource_name>'

def template_response(resp):
    template = flask.render_template('resource.xml', **resp)
    if resp.get('ok'):
        return template
    else:
        return template, resp['status']

class ResourceView(flask.views.MethodView):

    def get(self, subscription_id, cloud_service_name, resource_type, resource_name):
        body = xml_dict(request.data)
        result = ctrl.get(subscription_id, cloud_service_name, resource_name, resource_name, body)
        template_response(result)

    def post(self, subscription_id, cloud_service_name, resource_type, resource_name):
        body = xml_dict(request.data)
        result = ctrl.upgrade(subscription_id, cloud_service_name, resource_name, resource_name, body)
        template_response(result)

    def put(self, subscription_id, cloud_service_name, resource_type, resource_name):
        body = xml_dict(request.data)
        result = ctrl.create(subscription_id, cloud_service_name, resource_name, resource_name, body)
        template_response(result)

    def delete(self, subscription_id, cloud_service_name, resource_type, resource_name):
        body = xml_dict(request.data)
        ctrl.delete(subscription_id, cloud_service_name, resource_name, resource_name, body)
        template_response(result)

resources.add_url_rule(url, view_func=ResourceView.as_view('resource_view'))
