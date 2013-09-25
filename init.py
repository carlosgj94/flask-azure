import jinja2

envs = {
    # this is a live-fire exercise!
    'production': {},
    # a safe place for experimentation and self-expression
    'development': {}
}

for env, prompts in envs.iteritems():
    for field, prompt in prompts.iteritems():
        envs[env][field] = raw_input(prompt)

with open('templates/config.py', 'r') as f:
    template = jinja2.Template(f.read())

with open('config.py', 'w') as f:
    f.write(template.render(envs=envs))
    print 'Done!'