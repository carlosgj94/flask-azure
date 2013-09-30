import flask
from routes import add_routes_to

# vanilla app for your testing pleasure
app = flask.Flask(__name__)
add_routes_to(app)

# or, make your own!
def create_app(config):
    app = flask.Flask(__name__)
    app.config.update(config)
    add_routes_to(app)
    return app

if __name__ == '__main__':
    app.run()
