# Enter script code
import re
if re.match('.*(Emacs|Gnome-terminal|konsole)', window.get_active_class()):
    pass
else:
    store.set_global_value('shift_on', False)
