# Enter script code
import re
if re.match('.*(Emacs|Gnome-terminal|konsole)', window.get_active_class()):
    keyboard.send_keys('<ctrl>+ ')
else:
    sh_on = store.get_global_value('shift_on')

    if sh_on is None or not sh_on:
        # turn it on
        #keyboard.press_key('<shift>')
        store.set_global_value('shift_on', True)
    else:
        # turn it off
        #keyboard.release_key('<shift>')
        store.set_global_value('shift_on', False)
        