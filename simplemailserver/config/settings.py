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

#If using hooks inside a django project we need to point to the django project settings file
#in order to use django models
import os
os.environ['DJANGO_SETTINGS_MODULE']= 'djangoexample.settings'


#Hooks are defined by destination host and destination address pattern
#Each host can have different patterns, and each pattern has a hook defined that handles a message.
#A hook is a callable that accepts three arguments message, address, host.
#Any message to 123-123-123@localhost will be handled by handle_inportant
#Any message to 123-123@localhost will be handled by handle_junk
#any other address pattern including these will be forwarded to the relay
hooks = {
    'localhost' : ((r'(\d+)-(\d+)-(\d+)', 'djangoexample.mailhandler.hooks.handle_important'), 
        (r'(\d+)-(\d+)', 'djangoexample.mailhandler.hooks.handle_junk'))
}


# the config/boot.py will turn these values into variables set in settings
