import subprocess, platform, getpass, os, importlib

from core_commands import  Module_Commands


class aaf_tool(Module_Commands):


    def do_user(self, args):
        """Prints the current user"""
        print(getpass.getuser())

    def do_os(self, args):
        """Prints the current operating system"""
        print(platform.system())

    def do_dumpzilla(self, args):

        cwd = os.getcwd()
        print(cwd)
        path = cwd + "/dumpzilla"
        os.chdir(path)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        #option to manauly set
        defloc = subprocess.check_output("find  $HOME/.mozilla -type d -name "'*.default'"", shell=True)

        cmdargs = input("Enter arguments for dumpzilla: ")

        lindzcmd = 'python ' + dir_path + '/dumpzilla.py ' + defloc.rstrip() + " " + "" + cmdargs + ""
        p = subprocess.Popen(lindzcmd, shell=True)

    def do_hindsight(self, args):
        """hindsignt help stuff"""
        
        dir_path = os.path.dirname(os.path.realpath(__file__))

        cmdargs = input('Enter arguments for hindsight: ')
        print(cmdargs)

        cmdhsLinux = '/' + getpass.getuser() + '/.config/google-chrome/Default'

        linhscmd = 'python ' + dir_path + '/hindsight_master/hindsight.py -i ' + cmdhsLinux + " " + "" + cmdargs + ""

        print(linhscmd)
        theos = platform.system()

        if theos == "Linux":
            p = subprocess.Popen(linhscmd, shell=True)

    def do_getout(self, args):
        """Exits the program"""
        print ("Exiting AAF")
        raise SystemExit

    def do_use(self, mod_name):
        print("use this tools")
        module_shell = Module_Commands()
        module_shell.prompt = mod_name + " >"
        module_shell.cmdloop("boop letsgo")





if __name__ == '__main__':


    aaf_shell = aaf_tool()
    aaf_shell.prompt = 'AAF>> '
    aaf_shell.cmdloop("Starting BANNER")
