import sys
import gdb
banner =  '''
 /$$$$$$$                            /$$                        
 | $$__  $$                          | $$                        
 | $$  \ $$  /$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$/$$$$ 
 | $$$$$$$/ |____  $$| $$__  $$ /$$__  $$ /$$__  $$| $$_  $$_  $$
 | $$__  $$  /$$$$$$$| $$  \ $$| $$  | $$| $$  \ $$| $$ \ $$ \ $$
 | $$  \ $$ /$$__  $$| $$  | $$| $$  | $$| $$  | $$| $$ | $$ | $$
 | $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$
 |__/  |__/ \_______/|__/  |__/ \_______/ \______/ |__/ |__/ |__/

                                                      @Sigma-team
'''

class Banner(gdb.Command):
    '''
        print banner by R4naom
    '''
    def  __init__(self):
        super(Banner,self).__init__("banner", gdb.COMMAND_NONE)
    
    def invoke(self, arg, from_tty):
        self.show()

    def show(self, color="green"):
        #msg function belongs to peda module
        gdb.execute('shell clear')
        msg(banner, color)

gdb.execute('shell clear')
b = Banner()
msg(banner, "green")

