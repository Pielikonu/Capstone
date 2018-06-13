import subprocess, platform, getpass, os, sys
from cmd import Cmd

class cprompt(Cmd):

    def do_list(self, args):
        """Prints list of available tools"""
        print('Hindsight')
        print('Dumpzilla')

    def do_user(self, args):
        """Prints the current user"""
        print(getpass.getuser())

    def do_os(self, args):
        """Prints the current operating system"""
        print(platform.system())

    def do_dumpzilla(self, args):
        """ Options:
 --All (Shows everything but the DOM data. Doesn't extract thumbnails or HTML 5 offline)
 --Cookies [-showdom -domain <string> -name <string> -hostcookie <string> -access <date> -create <date> -secure <0/1> -httponly <0/1> -range_last -range_create <start> <end>]
 --Permissions [-host <string>]
 --Downloads [-range <start> <end>]
 --Forms	[-value <string> -range_forms <start> <end>]
 --History [-url <string> -title <string> -date <date> -range_history <start> <end> -frequency]
 --Bookmarks [-range_bookmarks <start> <end>]
 --Cacheoffline [-range_cacheoff <start> <end> -extract <directory>]
 --Thumbnails [-extract_thumb <directory>]
 --Range <start date> <end date>
 --Addons
 --Passwords (Decode only in Unix)
 --Certoverride
 --Session
 --Watch [-text <string>] (Shows in daemon mode the URLs and text form in real time. -text' Option allow filter,  support all grep Wildcards. Exit: Ctrl + C. only Unix).
"""
	cwd = os.getcwd()
	path = cwd + '/dumpzilla'
	os.chdir(path)
	dir_path = os.path.dirname(os.path.realpath(__file__))

	defloc = subprocess.check_output("find  $HOME/.mozilla -type d -name "'*.default'"", shell=True)
	cmdargs = raw_input('Enter arguments for dumpzilla: ')

	lindzcmd = 'python ' + dir_path + '/dumpzilla.py ' + defloc.rstrip() + " " + "" + cmdargs + ""
	p = subprocess.Popen(lindzcmd, shell=True)

    def do_hindsight(self, args):
        """  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to the Chrome(ium) "Default" directory
  -o OUTPUT, --output OUTPUT
                        Name of the output file (without extension)
  -b {Chrome,Brave}, --browser_type {Chrome,Brave}
                        Type of input files
  -f {sqlite,xlsx}, --format {sqlite,xlsx}
                        Output format
  -l LOG, --log LOG     Location Hindsight should log to (will append if exists)
  -t TIMEZONE, --timezone TIMEZONE
                        Display timezone for the timestamps in XLSX output
  -d {mac,linux}, --decrypt {mac,linux}
                        Try to decrypt Chrome data from a Linux or Mac system; support for both is currently buggy and enabling this may cause
                        problems. Only use "--decrypt linux" on data from a Linux system, and only use "--decrypt mac" when running Hindsight on the
                        same Mac the Chrome data is from.
  -c CACHE, --cache CACHE
                        Path to the cache directory; only needed if the directory is outside the given "input" directory. Mac systems are setup this
                        way by default.
"""
        
        dir_path = os.path.dirname(os.path.realpath(__file__))

	cmdargs = raw_input('Enter arguments for hindsight: ')
	print(cmdargs)

        cmdhsLinux = '/' + getpass.getuser() + '/.config/google-chrome/Default'

        linhscmd = 'python ' + dir_path + '/hindsight_master/hindsight.py -i ' + cmdhsLinux + " " + "" + cmdargs + "" 

        print(linhscmd)
        theos = platform.system()

        if theos == "Linux": 
            p = subprocess.Popen(linhscmd, shell=True)

    def do_getout(self, args):
        """Exits the program"""
        print ("Exiting.")
        raise SystemExit

if __name__ == '__main__':
    prompt = cprompt()
    prompt.prompt = 'aaf>> '
    prompt.cmdloop('''Starting...''')
