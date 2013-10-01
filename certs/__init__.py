from OpenSSL import SSL
import os

cwd = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')


def get_context(env):
    context = SSL.Context(SSL.SSLv23_METHOD)
    context.use_privatekey_file(os.path.join(cwd, 'private.key'))
    context.use_certificate_file(os.path.join(cwd, '%s.cer' % env))
    return context
