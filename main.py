#forked from linuxhint: https://linuxhint.com/create-simple-application-python-and-gtk3/
#import statements
import gi
gi.require_version("Gtk", "3.0")
gi.require_version('Notify', '0.7')
from gi.repository import Gtk
from gi.repository import Notify





#Initialize the environment

window = Gtk.Window(title="Didactic Succotash")
window.set_default_size(self,640,480)




window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()