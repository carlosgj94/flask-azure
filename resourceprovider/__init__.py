import flask
from routes import add_routes_to

app = flask.Flask(__name__)

add_routes_to(app)

if __name__ == '__main__':
    app.run()
