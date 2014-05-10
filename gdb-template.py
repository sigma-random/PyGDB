import sys
import gdb
gdb.execute('file /bin/cat')
o = gdb.execute('disassemble exit', to_string=True)
print o
print sys.path
gdb.execute('quit')
