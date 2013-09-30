from config import manifest
import jinja2

with open('templates/manifest.xml', 'r') as f:
    template = jinja2.Template(f.read())

with open('manifest.xml', 'w') as f:
    f.write(template.render(**manifest))

print "Created manifest.xml"