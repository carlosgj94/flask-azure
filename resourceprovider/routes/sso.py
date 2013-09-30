import flask
from resourceprovider.controllers import sso as ctrl

sso = flask.Blueprint('sso', __name__)
url = '/subscriptions/<subscription_id>/cloudservices/<cloud_service_name>'

@sso.route('/subscriptions/<subscription_id>/cloudservices/<cloud_service_name>/resources/<resource_type>/<resource_name>/SsoToken', methods=['POST'])
def create_sso(subscription_id, cloud_service_name, resource_type, resource_name):
    try:
        result = ctrl.create(subscription_id, cloud_service_name, resource_type, resource_name)
    except NotImplementedError as e:
        return flask.abort(500)
    else:
        return flask.render_template('sso.xml', **result)

@sso.route('/sso', methods=['GET'])
def get_sso():
    try:
        result = ctrl.get(**flask.request.args)
    except NotImplementedError as e:
        return flask.abort(500)
    else:
        return flask.render_template('sso.xml', **result)