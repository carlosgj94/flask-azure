import flask
import flask.views
from flask import request
from resourceprovider.controllers import resources as ctrl

resources = flask.Blueprint('resources', __name__)
url = '/subscriptions/<subscription_id>/cloudservices/<cloud_service_name>/resources/<resource_type>/<resource_name>'

class ResourceView(flask.views.MethodView):
    def get(self, subscription_id, cloud_service_name, resource_type, resource_name):
        raise NotImplementedError

    def post(self, subscription_id, cloud_service_name, resource_type, resource_name):
        raise NotImplementedError

    def put(self, subscription_id, cloud_service_name, resource_type, resource_name):
        raise NotImplementedError

    def delete(self, subscription_id, cloud_service_name, resource_type, resource_name):
        raise NotImplementedError

resources.add_url_rule(url, view_func=ResourceView.as_view('resource_view'))
