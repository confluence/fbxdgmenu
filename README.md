fbxdgmenu.py
============

This is a script which generates an applications menu for Fluxbox using
the freedesktop.org (XDG) standard. It requires the pyxdg library. By
default the menu is generated as a submenu which can be included in a
hand-maintained main fluxbox menu.  There is another project which
generates a more fancy XDG Fluxbox menu [1]; I wrote this partially to
understand how the XDG menu works, but also to have a simpler script
which handles *only* the applications menu.

Usage examples:
---------------

To generate a menu:

    fbxdgmenu.py > ~/.fluxbox/applications-menu

Menu entry for including a generated submenu:

    [include] (YOUR_HOME_DIR/.fluxbox/applications-menu)

Menu entry for regenerating the menu:

    [exec] (Regenerate menu) {/PATH/TO/fbxdgmenu.py > YOUR_HOME_DIR/.fluxbox/applications-menu}

Known issues:
-------------

By default, the xdg library looks for a menu file in `/etc/xdg/menus/debian-menu.menu`, which may not be present on your system by default: for example, on Ubuntu this file is provided by the `menu-xdg` package. If you do not wish to use this file, you may also specify an explicit path to another menu file as a parameter to the script:

    fbxdgmenu.py /etc/xdg/menus/some-other.menu > ~/.fluxbox/applications-menu

I recommend `/etc/xdg/menus/gnome-applications.menu`, which provides a very complete list of installed applications.

[1] fluxbox-xdg-menu can also generate a wallpaper submenu, and has a header and footer that you may find useful. https://code.google.com/p/fluxbox-xdg-menu/
