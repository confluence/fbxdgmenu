#!/usr/bin/env python

from xdg import Menu, IconTheme
import sys

STANDALONE=False

TERMINAL_COMMAND = "konsole -e %s"
TERMINAL_PATH_COMMAND = "konsole --workdir %s -e %s"

ICON_THEMES = ('gnome', 'oxygen', 'hicolor')

class FluxboxXDGMenu:
    def __init__(self, standalone=False, filename=None):
        menu = Menu.parse(filename)

        if standalone:
            self.contents = "[begin] (Fluxbox)"
            self.contents.extend(self.menu(menu, depth=1))
            self.comtents.append("[end]")
        else:
            self.contents = self.menu(menu)

    def __str__(self):
        return "\n".join(self.contents)

    # TODO: add a hack to look for more icons in /opt/something and /usr/share/app-install/icons
    def _find_icon(self, icon_name):
        for theme in ICON_THEMES:
            icon = IconTheme.getIconPath(icon_name, theme=theme, extensions=['png', 'xpm'])
            if icon:
                return icon

        if not icon:
            return ""

    def menu(self, menu, depth=0):
        contents = []

        indent = " " * 4 * depth
        name = menu.getName().encode("utf8")
        icon = self._find_icon(menu.getIcon()) or ""
        contents.append("%s[submenu] (%s) <%s>" % (indent, name, icon))

        for entry in menu.getEntries():
            if isinstance(entry, Menu.MenuEntry):
                try:
                    contents.append(self.entry(entry, depth + 1))
                except ValueError, e:
                    sys.stderr.write(str(e))
                    continue
            elif isinstance(entry, Menu.Menu):
                contents.extend(self.menu(entry, depth + 1))
            elif isinstance(entry, Menu.Separator):
                contents.append(self.separator(depth + 1))

        contents.append("%s[end]" % indent)

        return contents

    def entry(self, entry, depth):
        indent = " " * 4 * depth
        name = entry.DesktopEntry.getName().encode("utf8")
        icon = self._find_icon(entry.DesktopEntry.getIcon()) or ""

        d_exec = entry.DesktopEntry.getExec()
        if not d_exec:
            raise ValueError("No executable information found for entry '%s' (%s)." % (name, entry))

        executable = d_exec.split()[0]
        path = entry.DesktopEntry.getPath()
        terminal = entry.DesktopEntry.getTerminal()

        if path and terminal:
            command = TERMINAL_PATH_COMMAND % (path, executable)
        elif terminal: # and not path
            command = TERMINAL_COMMAND % executable
        elif path: # and not terminal
            command = "cd %s; %s" % (path, executable)
        else: # if neither
            command = executable

        return "%s[exec] (%s) {%s} <%s>" % (indent, name, command, icon)

    def separator(self, depth):
        indent = " " * 4 * depth
        return "%s[separator]" % indent

filename = sys.argv[1] if len(sys.argv) > 1 else None
print FluxboxXDGMenu(standalone=STANDALONE, filename=filename)
