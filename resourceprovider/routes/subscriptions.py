import flask
import flask.views
from flask import request
from resourceprovider.util import xml_dict
from resourceprovider.controllers import subscriptions as ctrl

subscriptions = flask.Blueprint('subscriptions', __name__)


@subscriptions.route('/subscriptions/<subscription_id>/Events', methods=['POST'])
def subscribe(subscription_id):
    """
    handle subscription events: Registered, Disabled, Enabled, Deleted
    """
    body = xml_dict(request.data)
    event = body['EntityState'] or body['EntityEvent']
    if event == 'Registered':
        ctrl.registered(subscription_id, body)
    elif event == 'Disabled':
        ctrl.disabled(subscription_id, body)
    elif event == 'Enabled':
        ctrl.enabled(subscription_id, body)
    elif event == 'Deleted':
        ctrl.deleted(subscription_id, body)
    else:
        flask.abort(400)
