import re
import logging
from lamson.routing import route, route_like, stateless
from config.settings import relay, hooks
from lamson import view

def _get_hook(name):
    components = name.split('.')
    mod = __import__( '.'.join(components[:-1]))
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

@route("(address)@(host)", address=".+")
@stateless
def HOOK(message, address=None, host=None):
    for hook in hooks.get(host, []):
        if re.compile(hook[0]).match(address):
            hook_function = _get_hook(hook[1])
            hook_function(message, address, host)
        

@route_like(HOOK)
@stateless
def FORWARD(message, address=None, host=None):
    relay.deliver(message)

