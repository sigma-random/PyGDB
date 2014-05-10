
try:
	import gdb
except Exception,e:
	print e



sizeAliasMap = {1:'b',2:'h',4:'w',8:'g'}
registers    = ['eax','ebx','ecx','edx','esi','edi','eip','esp','ebp','cs','es','ds','ss','fs']


'''
struct pt_regs {
	long ebx;
	long ecx;
	long edx;
	long esi;
	long edi;
	long ebp;
	long eax;
	int  xds;
	int  xes;
	int  xfs;
	int  xgs;
	long orig_eax;
	long eip;
	int  xcs;
	long eflags;
	long esp;
	int  xss;
};
'''

pt_regs_info ={
'ebx':('long',4),
'ecx':('long',4),
'edx':('long',4),
'esi':('long',4),
'edi':('long',4),
'ebp':('long',4),
'eax':('long',4),
'xds':('int',4),
'xes':('int',4),
'xfs':('int',4),
'xgs':('int',4),
'orig_eax':('long',4),
'eip':('long',4),
'xcs':('int',4),
'eflags':('long',4),
'esp':('long',4),
'xss':('int',4)
}


struct_map = {
	'pt_regs':pt_regs_info

}

def getRegisterValue(reg):
	try:
		print type(gdb.parse_and_eval("$esp"))
		result = gdb.parse_and_eval("$esp")
		print result
	except Exception,e:
		print(str(e))
		raise gdb.GdbError('make sure program has run!')

def isRegister(input):
	if input[0] != '$':
		return False
	if input[1:] in registers:
		return True
	return False

def checkStruct(st_name):
	if st_name in struct_map.keys():
		return True
	else:
		raise gdb.GdbError('no struct named %s'%st_name)
		return False

def getStructInstance(st_name): return struct_map[st_name]


def getStructSize(st_instance):
	field_list = st_instance.keys()
	return sum([size for (_,size) in pt_regs_info.values()])


def parseStruct(st):

	pass

def getSizeAlias(size):
	if size not in sizeAliasMap.keys():
		return 'b'
	return sizeAliasMap[size]


class StructHelper(gdb.Command):
	"""print struct"""

	def __init__ (self):
		gdb.write('StructHelper',gdb.STDOUT)
		super(StructHelper,self).__init__ ( "struct", gdb.COMMAND_DATA)

	def invoke (self, arg, from_tty):
		argv =  gdb.string_to_argv(arg)
		if len(argv) != 2:
			raise gdb.GdbError('usage: struct struct_name address\n')
		st_name = argv[0]
		address = getRegisterValue(argv[1]) if isRegister(argv[1]) else long(argv[1])

		print address
		if checkStruct(st_name):
			self.dumpStructMem(st_name, address)

		

	def dumpStructMem(self,st_name, address):
		st_instance = getStructInstance(st_name)
		dumpAddr = address
		for (name,(type,size)) in st_instance.items():
			sizename = getSizeAlias(size)
			dump_cmd = 'x/x%c %s'%(sizename,dumpAddr)
			print dump_cmd

			try:
				result = gdb.execute(dump_cmd, to_string=True)
				print result
			except Exception,e:
				raise gdb.GdbError(e)

			#dumpAddr += size
			return



StructHelper()
