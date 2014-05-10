import gdb

class HelloWorld (gdb.Command):
	"""Greet the whole world."""

	def __init__ (self):
		#gdb.Command.__init__ (self, "hello", gdb.COMMAND_DATA)
		super(HelloWorld,self).__init__ ( "hello", gdb.COMMAND_DATA)

	def invoke (self, arg, from_tty):
		print "Hello, World!"

HelloWorld ()
