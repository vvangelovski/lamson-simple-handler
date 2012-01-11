from models import ReceivedMessage

def store_message(message, to_address, tag):
    msg = ReceivedMessage(tag = tag, content = message.body(), subject = message.base['Subject'], to_address = to_address, from_address = message.base['From'])
    msg.save()

def handle_important(message, address=None, host=None):
    store_message(message, "%s@%s"%(address, host), 'important')


def handle_junk(message, address=None, host=None):
    store_message(message, "%s@%s"%(address, host), 'junk')


