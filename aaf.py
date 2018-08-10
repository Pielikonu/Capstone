import subprocess, platform, getpass, os, sys
import yaml
from cmd import Cmd

class cprompt(Cmd):

    def do_list(self, args):
        """Prints list of available tools"""
        print('hindsight')
        print('dumpzilla')

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

        stream = open("config.yml", 'r')
        dzconfig = yaml.load(stream)
        dhistory = (dzconfig['cfdumpzilla']['dhistory'])
        dbookmarks = (dzconfig['cfdumpzilla']['dbookmarks'])

	print("Current options set for Dumpzilla:\n")
	optionlist = [('History', dhistory),
           	('Bookmarks', dbookmarks)]
	header = u"{0:<20}{1:>6}".format('Option','Value')
	print(header)
	print("-"*len(header))
	for option, value in optionlist:
		print(u"{0:<20}{1:>6}".format(option, value))

        cwd = os.getcwd()
        path = cwd + '/dumpzilla'
        os.chdir(path)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        defloc = subprocess.check_output("find  $HOME/.mozilla -type d -name "'*.default'"", shell=True)

	contedit = raw_input("\nExecute with these options? y/n: ")
	if contedit in ['y', 'Y']:
        	lindzcmd = 'python ' + dir_path + '/dumpzilla.py ' + defloc.rstrip() + " " + dhistory + " " + dbookmarks
        	p = subprocess.Popen(lindzcmd, shell=True)
	else: 
		while contedit in ['n', 'N']:
			selectop = raw_input("\nWhich option do you want to change? (Type done to finish editing) : ")
			if selectop in ['history', 'History']:
				houtput = raw_input("\nEnter url, date, title, or range: ")
			elif selectop in ['bookmarks', 'Bookmarks']:
				hformat = raw_input("\nEnter a range: ")
			elif selectop in ['done', 'Done']:
				contedit = 'y'
        			lindzcmd = 'python ' + dir_path + '/dumpzilla.py ' + defloc.rstrip() + " " + dhistory + " " + dbookmarks
        			p = subprocess.Popen(lindzcmd, shell=True)


    def do_hindsight(self, args):
        """  Options:
  -h, --help            show this help message and exit
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

        stream = open("config.yml", 'r')
        hsconfig = yaml.load(stream)
        hformat = (hsconfig['cfhindsight']['hformat'])
        houtput = (hsconfig['cfhindsight']['houtput'])


        dir_path = os.path.dirname(os.path.realpath(__file__))
        cmdhsLinux = '/' + getpass.getuser() + '/.config/google-chrome/Default'


	print("Current options set for Hindsight:\n")
	optionlist = [('Format', hformat),
           	('Output', houtput)]
	header = u"{0:<20}{1:>6}".format('Option','Value')
	print(header)
	print("-"*len(header))
	for option, value in optionlist:
		print(u"{0:<20}{1:>6}".format(option, value))


	contedit = raw_input("\nExecute with these options? y/n: ")
	if contedit in ['y', 'Y']:
		linhscmd = 'python ' + dir_path + '/hindsight_master/hindsight.py -i ' + cmdhsLinux + " " + houtput + " " + hformat
		p = subprocess.Popen(linhscmd, shell=True)
	else: 
		while contedit in ['n', 'N']:
			selectop = raw_input("\nWhich option do you want to change? (Type done to finish editing) : ")
			if selectop in ['output', 'Output']:
				houtput = raw_input("\nEnter new output path (include -o but do not include file extension): ")
			elif selectop in ['format', 'Format']:
				hformat = raw_input("\nSpecify the format (-f sqlite or -f xlsx): ")
			elif selectop in ['done', 'Done']:
				contedit = 'y'
				linhscmd = 'python ' + dir_path + '/hindsight_master/hindsight.py -i ' + cmdhsLinux + " " + houtput + " " + hformat
				p = subprocess.Popen(linhscmd, shell=True)


    def do_exit(self, args):
        """Exits the program"""
        print ("Exiting.")
        raise SystemExit

if __name__ == '__main__':
    prompt = cprompt()
    prompt.prompt = 'aaf>> '
    prompt.cmdloop('''Starting...''')
