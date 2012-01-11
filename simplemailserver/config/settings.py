# This file contains python variables that configure Lamson for email processing.
import logging

# You may add additional parameters such as `username' and `password' if your
# relay server requires authentication, `starttls' (boolean) or `ssl' (boolean)
# for secure connections.
relay_config = {'host': 'localhost', 'port': 8825}

receiver_config = {'host': 'localhost', 'port': 8823}

handlers = ['app.handlers.simple']

router_defaults = {'host': '.+'}

template_config = {'dir': 'app', 'module': 'templates'}

import os
os.environ['DJANGO_SETTINGS_MODULE']= 'djangoexample.settings'

hooks = {
    'localhost' : ((r'(\d+)-(\d+)-(\d+)', 'djangoexample.mailhandler.hooks.handle_important'), 
        (r'(\d+)-(\d+)', 'djangoexample.mailhandler.hooks.handle_junk'))
}


# the config/boot.py will turn these values into variables set in settings
