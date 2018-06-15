from cmd import Cmd
class Module_Commands(Cmd):
    def do_help(self,args):
        """Help overiding method"""
        print("help is overridden")

    def do_list(self, args):
        """Prints list of available tools"""
        print('Hindsight')
        print('Dumpzilla')


    def do_memes(self,args):
        """Prints Memes"""
        print ("memes " + args)

