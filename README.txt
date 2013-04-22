fbxdgmenu.py
------------

This is a script which generates an applications menu for Fluxbox using
the freedesktop.org (XDG) standard. It requires the pyxdg library. By
default the menu is generated as a submenu which can be included in a
hand-maintained main fluxbox menu.  There is another project which
generates a more fancy XDG Fluxbox menu [1]; I wrote this partially to
understand how the XDG menu works, but also to have a simpler script
which handles *only* the applications menu.

Usage examples:

To generate a menu:

    fbxdgmenu.py > ~/.fluxbox/applications-menu

Menu entry for including a generated submenu:

    [include] (YOUR_HOME_DIR/.fluxbox/applications-menu)

Menu entry for regenerating the menu:

    [exec] (Regenerate menu) {/PATH/TO/fbxdgmenu.py > YOUR_HOME_DIR/.fluxbox/menu}

Known issues:

* Helpful command-line options to follow. Suggestions welcome.
* To handle desktop entry field codes the script currently strips
everything except the first word out of the executable. This works for
most entries, but some will not be processed correctly.

[1] fluxbox-xdg-menu can also generate a wallpaper submenu, and has a
header and footer that you may find useful.
https://code.google.com/p/fluxbox-xdg-menu/
