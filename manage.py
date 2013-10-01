import resourceprovider
import config
import sys

# env defaults
defaults = {
    'development': {
        'use_debugger': True,
        'use_reloader': True
    }
}

def start_app(env="development"):
    options = config.app[env]
    options.update(defaults.get(env, {}))
    print options
    return resourceprovider.create_app(options)

if __name__ == "__main__":
	start_app(sys.argv[1]).run()