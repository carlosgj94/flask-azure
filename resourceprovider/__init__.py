import flask
from routes import add_routes_to


def create_app(config):
    app = flask.Flask(__name__)
    app.config.update(config)
    add_routes_to(app)
    return app

if __name__ == '__main__':
    create_app({}).run()
