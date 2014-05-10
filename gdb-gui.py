from threading import Thread
import gtk
import gdb

def printit ():
    print "Hello hacker"

class TestGtkThread (Thread):
    def destroy (self, *args):
        self.window.hide()

    def hello (self, *args):
        gdb.post_event (printit)

    def run (self):
        gtk.gdk.threads_init()

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)

        button = gtk.Button("Hello World")
        # connects the 'hello' function to the clicked signal from the button
        button.connect("clicked", self.hello)
        self.window.add(button)
        button.show()

        self.window.show_all()
        gtk.main()

class GdbGUI (gdb.Command):
    def __init__ (self):
        super (GdbGUI, self).__init__ ("gdb-gui", gdb.COMMAND_DATA,gdb.COMPLETE_NONE)
        self.init = False

    def invoke (self, arg, from_tty):
        self.dont_repeat()
        if not self.init:
            self.init = True
            v = TestGtkThread()
            v.setDaemon (True)
            v.start ()

GdbGUI()