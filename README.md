# autokey-emacs-config

Keybindings for AutoKey to provide Emacs goodness everywhere else. This config was originally based on https://github.com/hobbs/autokey-emacs-osx, but extended to include more navigation bindings, marking, and copying/pasting to mimic Emacs.

Original functionality is moved to make use of the <super> key (i.e., the Windows key) for keybindings (e.g., <super>-f replaces <ctrl>-f for the find command).

These scripts have only been tested with the Autokey (specifically autokey-gtk) available on Debian Testing, which was version 0.90.4 working with Python 2.7 as of this writing. That said, it should work just fine with the newer Python 3 port.


# Installation

I simply create a symbolic link to this directory holding the scripts anywhere inside `~/.config/autokey/` and it seems to work well.
