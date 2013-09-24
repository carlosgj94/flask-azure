from resources import resources
from subscriptions import subscriptions

def add_routes_to(app):
	for blueprint in [resources, subscriptions]:
		app.register_blueprint(blueprint)