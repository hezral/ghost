# window.py
#
# Copyright 2021 Adi Hezral
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
gi.require_version('Handy', '1')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Handy, Gdk, Gio

# @Gtk.Template(resource_path='/com/github/hezral/ghosts/window.ui')
class GhostsWindow(Handy.Window):
    __gtype_name__ = 'GhostsWindow'

    Handy.init()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        header = Handy.HeaderBar()
        header.props.show_close_button = True
        header.props.hexpand = True
        header.props.title = "HandyWindow"

        label = Gtk.Label("Ghosts")
        label.props.expand = True
        label.props.valign = label.props.halign = Gtk.Align.CENTER

        grid = Gtk.Grid()
        grid.props.expand = True
        grid.attach(header, 0, 0, 1, 1)
        grid.attach(label, 0, 1, 1, 1)

        self.add(grid)
        self.show_all()
        self.set_size_request(700, 450)
        self.connect("destroy", Gtk.main_quit)

