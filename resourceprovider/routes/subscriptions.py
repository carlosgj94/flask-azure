import flask
import flask.views
from flask import request
from resourceprovider.util import xml_dict
from resourceprovider.controllers import subscriptions as ctrl

subscriptions = flask.Blueprint('subscriptions', __name__)

events = {
    'Registered'    :   ctrl.registered,
    'Disabled'      :   ctrl.disabled,
    'Enabled'       :   ctrl.enabled,
    'Deleted'       :   ctrl.deleted
}

def template_response(resp):
    if resp.get('ok'):
        return '', resp['status']
    else:
        flask.abort(resp['status'])

@subscriptions.route('/subscriptions/<subscription_id>/Events', methods=['POST'])
def subscribe(subscription_id):
    """
    handle subscription events: Registered, Disabled, Enabled, Deleted
    """
    body = xml_dict(request.data)
    event = body['EntityState'] or body['EntityEvent']
    if event in events:
        result = events[event](subscription_id, body)
        template_response(result)
    else:
        flask.abort(400)