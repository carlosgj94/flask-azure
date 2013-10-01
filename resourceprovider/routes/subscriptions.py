import flask
import flask.views
from flask import request
from xml.etree import cElementTree as ElementTree
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
    body = ElementTree.fromstring(request.data)
    event = body.findall('{http://schemas.datacontract.org/2004/07/Microsoft.Cis.DevExp.Services.Rdfe.ServiceManagement}EntityState')[0]
    if event.text in events.keys():
        result = events[event.text](subscription_id, body)
        template_response(result)
    else:
        flask.abort(400)
