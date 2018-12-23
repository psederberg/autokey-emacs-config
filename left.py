# set the actions
hotkey = '<ctrl>+b'
newkey = '<left>'

# save the hotkey for pasthrough 
store.set_global_value('hotkey', hotkey)

# see if we're going to add shift
sh_on = store.get_global_value('shift_on')
if sh_on:
    # add shift
    sh_mod = '<shift>+'
else:
    sh_mod = ''
engine.set_return_value(sh_mod + newkey)

# proces the key
engine.run_script('process_key')

