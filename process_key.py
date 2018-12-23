# the magic script that gets called by all the others to filter and forward the key combo

#import logging # see the logs in ~/.config/autokey/autokey.log
import re

#logging.basicConfig(level=logging.DEBUG)
h = store.get_global_value('hotkey')
s =  engine.get_return_value()
#logging.debug("combo got: " + str(s)) # autokey-gtk -l

#logging.debug(window.get_active_class())

#if re.match('^((?!.*Emacs).)*$', window.get_active_class()):
if re.match('.*(Emacs|Guake|gnome-terminal|konsole)', window.get_active_class()):
    #logging.debug('passing through (%s) for %s' % (h, window.get_active_class()))
    keyboard.send_keys(h)
    store.set_global_value('ignored', True)
else:
    #logging.debug('replacing for: %s' % window.get_active_class())
    keyboard.send_keys(s)
    store.set_global_value('ignored', False)