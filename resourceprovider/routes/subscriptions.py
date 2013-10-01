import flask
import flask.views
from flask import request
import xmltodict
from resourceprovider.controllers import subscriptions as ctrl

subscriptions = flask.Blueprint('subscriptions', __name__)

events = {
    'Registered':   ctrl.registered,
    'Disabled':   ctrl.disabled,
    'Enabled':   ctrl.enabled,
    'Deleted':   ctrl.deleted
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
    body = xmltodict.parse(request.data)
    event = body['EntityEvent']['EntityState']
    if event in events.keys():
        result = events[event](subscription_id, body)
        template_response(result)
    else:
        flask.abort(400)
