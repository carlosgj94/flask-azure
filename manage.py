from flask.ext.script import Manager, Server
import resourceprovider
import config

manager = Manager(resourceprovider.app)

# env defaults
defaults = {
    'development': {
        'use_debugger': True,
        'use_reloader': True
    }
}

for env, opts in config.app.iteritems():
    options = defaults.get(env, {})
    options.update(opts)
    manager.add_command(env, Server(**options))

if __name__ == "__main__":
	manager.run()