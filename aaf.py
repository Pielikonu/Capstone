import subprocess, platform, getpass, os, sys
import yaml
from cmd import Cmd

def dumpzilla():
        dir_path = os.path.dirname(os.path.realpath(__file__))

	stream = open(dir_path + "/dumpzilla/config.yml", 'r')
       	dzconfig = yaml.load(stream)
	daddons = (dzconfig['cfdumpzilla']['Addons'])
	dall = (dzconfig['cfdumpzilla']['All'])
       	dbookmarks = (dzconfig['cfdumpzilla']['Bookmarks'])
	dcacheoffline = (dzconfig['cfdumpzilla']['Cacheoffline'])
	dcertoverride = (dzconfig['cfdumpzilla']['Certoverride'])
       	dcookies = (dzconfig['cfdumpzilla']['Cookies'])
	ddownloads = (dzconfig['cfdumpzilla']['Downloads'])
	dforms = (dzconfig['cfdumpzilla']['Forms'])
       	dhistory = (dzconfig['cfdumpzilla']['History'])
	dpasswords = (dzconfig['cfdumpzilla']['Passwords'])
	dpermissions = (dzconfig['cfdumpzilla']['Permissions'])
	drange = (dzconfig['cfdumpzilla']['Range'])
	dsession = (dzconfig['cfdumpzilla']['Session'])
	dthumbnails = (dzconfig['cfdumpzilla']['Thumbnails'])
	dwatch = (dzconfig['cfdumpzilla']['Watch'])

	if daddons is None:
		daddons = ''
	if dall is None:
		dall = ''
	if dbookmarks is None:
		dbookmarks = ''
	if dcacheoffline is None:
		cacheoffline = ''
	if dcertoverride is None:
		dcertoverride = ''
	if dcookies is None:
		dcookies = ''
	if ddownloads is None:
		ddownloads = ''
	if dforms is None:
		dforms = ''
	if dhistory is None:
		dhistory = ''
	if dpasswords is None:
		dpasswords = ''
	if dpermissions is None:
		dpermissions = ''
	if drange is None:
		drange = ''
	if dsession is None:
		dsession = ''
	if dthumbnails is None:
		dthumbnails = ''
	if dwatch is None:
		dwatch = ''

        cwd = os.getcwd()
        path = cwd + '/dumpzilla'
        os.chdir(path)
        defloc = subprocess.check_output("find  $HOME/.mozilla -type d -name "'*.default'"", shell=True)
        
	lindzcmd = 'python ' + dir_path + '/dumpzilla/dumpzilla.py ' + defloc.rstrip() + " " + dhistory + " " + dbookmarks + " " + dcookies
        p = subprocess.Popen(lindzcmd, shell=True)

def hindsight():
        dir_path = os.path.dirname(os.path.realpath(__file__))

       	stream = open(dir_path + "/hindsight_master/config.yml", 'r')
       	hsconfig = yaml.load(stream)
	hbrowser = (hsconfig['cfhindsight']['Browser'])
	hcache = (hsconfig['cfhindsight']['Cache'])
	hdecrypt = (hsconfig['cfhindsight']['Decrypt'])
       	hformat = (hsconfig['cfhindsight']['Format'])
	hlog = (hsconfig['cfhindsight']['Log'])
        houtput = (hsconfig['cfhindsight']['Output'])
	htimezone = (hsconfig['cfhindsight']['Timezone'])

	if hbrowser is None:
		hbrowser = ''
	if hcache is None:
		hcache = ''
	if hdecrypt is None:
		hdecrypt = ''
	if hformat is None:
		hformat = ''
	if hlog is None:
		hlog = ''
	if houtput is None:
		houtput = ''
	if htimezone is None:
		htimezone = ''

        cmdhsLinux = '/' + getpass.getuser() + '/.config/google-chrome/Default'

	linhscmd = 'python ' + dir_path + '/hindsight_master/hindsight.py -i ' + cmdhsLinux + " " + houtput + " " + hformat + " " + hbrowser + " " + hcache + " " + hdecrypt + " " + hlog + " " + htimezone
	p = subprocess.Popen(linhscmd, shell=True)

def evtx():
        dir_path = os.path.dirname(os.path.realpath(__file__))

	stream = open(dir_path + "/python_evtx_master/config.yml", 'r')
        econfig = yaml.load(stream)
        einput = (econfig['cfevtx']['Input'])
        eoutput = (econfig['cfevtx']['Output'])

	if einput is None:
		einput = ''
	if eoutput is None:
		eoutput = ''

        cwd = os.getcwd()
        path = cwd + '/python_evtx_master/scripts'
        os.chdir(path)

	print("---Executing Evtx parser---")
        linevcmd = 'python ' + dir_path + '/python_evtx_master/scripts/evtx_dump.py' + " " + einput + " >" + " " + eoutput
        p = subprocess.Popen(linevcmd, shell=True)

class cprompt(Cmd):
     context = "aaf"

     def do_list(self, args):
	"""Prints list of available tools"""
        print('\nhindsight')
        print('dumpzilla')
	print('evtx\n')

     def do_use(self, tool):
	"""Type use <tool> to use a tool"""
	self.context = tool
	if tool in ['dumpzilla', 'Dumpzilla']:
		self.prompt = 'aaf/' + tool + '>> '
	elif tool in ['hindsight', 'Hindsight']:
		self.prompt = 'aaf/' + tool + '>> '
	elif tool in ['evtx', 'Evtx']:
		self.prompt = 'aaf/' + tool + '>> '
	else:
		print("\nError: Tool does not exist! Use the list command to view a list of tools.\n")

     def do_options(self, tool):
	"""Shows the current options set when a tool is in use"""
        cwd = os.getcwd()
        path = cwd + '/' + self.context
	if self.context in ['dumpzilla', 'Dumpzilla']:
		stream = open(path + "/config.yml", 'r')
        	dzconfig = yaml.load(stream)
		daddons = (dzconfig['cfdumpzilla']['Addons'])
		dall = (dzconfig['cfdumpzilla']['All'])
        	dbookmarks = (dzconfig['cfdumpzilla']['Bookmarks'])
		dcacheoffline = (dzconfig['cfdumpzilla']['Cacheoffline'])
		dcertoverride = (dzconfig['cfdumpzilla']['Certoverride'])
        	dcookies = (dzconfig['cfdumpzilla']['Cookies'])
		ddownloads = (dzconfig['cfdumpzilla']['Downloads'])
		dforms = (dzconfig['cfdumpzilla']['Forms'])
        	dhistory = (dzconfig['cfdumpzilla']['History'])
		dpasswords = (dzconfig['cfdumpzilla']['Passwords'])
		dpermissions = (dzconfig['cfdumpzilla']['Permissions'])
		drange = (dzconfig['cfdumpzilla']['Range'])
		dsession = (dzconfig['cfdumpzilla']['Session'])
		dthumbnails = (dzconfig['cfdumpzilla']['Thumbnails'])
		dwatch = (dzconfig['cfdumpzilla']['Watch'])
		
		print("\nCurrent options set for Dumpzilla:\n")
		optionlist = [('Addons', daddons),
           		('All', dall),
			('Bookmarks', dbookmarks),
			('Cacheoffline', dcacheoffline),
			('Certoverride', dcertoverride),
			('Cookies', dcookies),
			('Downloads', ddownloads),
			('Forms', dforms),
			('History', dhistory),
			('Passwords', dpasswords),
			('Permissions', dpermissions),
			('Range', drange),
			('Session', dsession),
			('Thumbnails', dthumbnails),
			('Watch', dwatch)]
		header = u"{0:<20}{1:>6}".format('Option','Value')
		print(header)
		print("-"*len(header))
		for option, value in optionlist:
			print(u"{0:<20}{1:>6}".format(option, value) + '\n')

	elif self.context in ['hindsight', 'Hindsight']:
        	stream = open(path + "_master/config.yml", 'r')
        	hsconfig = yaml.load(stream)
		hbrowser = (hsconfig['cfhindsight']['Browser'])
		hcache = (hsconfig['cfhindsight']['Cache'])
		hdecrypt = (hsconfig['cfhindsight']['Decrypt'])
        	hformat = (hsconfig['cfhindsight']['Format'])
		hlog = (hsconfig['cfhindsight']['Log'])
	        houtput = (hsconfig['cfhindsight']['Output'])
		htimezone = (hsconfig['cfhindsight']['Timezone'])

		print("\nCurrent options set for Hindsight:\n")
		optionlist = [('Browser', hbrowser),
           		('Cache', hcache),
			('Decrypt', hdecrypt),
			('Format', hformat),
			('Log', hlog),
			('Output', houtput),
			('Timezone', htimezone)]
		header = u"{0:<20}{1:>6}".format('Option','Value')
		print(header)
		print("-"*len(header))
		for option, value in optionlist:
			print(u"{0:<20}{1:>6}".format(option, value) + '\n')

	elif self.context in ['evtx', 'Evtx']:
		stream = open(cwd + "/python_evtx_master/config.yml", 'r')
        	econfig = yaml.load(stream)
        	einput = (econfig['cfevtx']['Input'])
        	eoutput = (econfig['cfevtx']['Output'])

		print("\nCurrent options set for Evtx:\n")
		optionlist = [('Input', einput),
           		('Output', eoutput)]
		header = u"{0:<20}{1:>6}".format('Option','Value')
		print(header)
		print("-"*len(header))
		for option, value in optionlist:
			print(u"{0:<20}{1:>6}".format(option, value) + '\n')

     def do_set(self, line):
        cwd = os.getcwd()
        path = cwd + '/' + self.context
	if self.context in ['dumpzilla', 'Dumpzilla']:
		option,value = [str(s) for s in line.split()]
    		with open(path + '/config.yml') as f:
        		doc = yaml.load(f)
		doc['cfdumpzilla'][option] = value
		with open(path + '/config.yml', 'w') as f:
        		yaml.dump(doc, f)

	elif self.context in ['hindsight', 'Hindsight']:
		option,letter,value = [str(s) for s in line.split()]
    		with open(path + '_master/config.yml') as f:
        		doc = yaml.load(f)
		doc['cfhindsight'][option] = letter + " " + value
		with open(path + '_master/config.yml', 'w') as f:
        		yaml.dump(doc, f)

	elif self.context in ['evtx', 'Evtx']:
		option,value = [str(s) for s in line.split()]
    		with open(cwd + '/python_evtx_master/config.yml') as f:
        		doc = yaml.load(f)
		doc['cfevtx'][option] = value
		with open(cwd + '/python_evtx_master/config.yml', 'w') as f:
        		yaml.dump(doc, f)

     def do_unset(self, option):
	cwd = os.getcwd()
        path = cwd + '/' + self.context
	if self.context in ['dumpzilla', 'Dumpzilla']:
    		with open(path + '/config.yml') as f:
        		doc = yaml.load(f)
		doc['cfdumpzilla'][option] = None
		with open(path + '/config.yml', 'w') as f:
        		yaml.dump(doc, f)

	elif self.context in ['hindsight', 'Hindsight']:
    		with open(path + '_master/config.yml') as f:
        		doc = yaml.load(f)
		doc['cfhindsight'][option] = None
		with open(path + '_master/config.yml', 'w') as f:
        		yaml.dump(doc, f)

	elif self.context in ['evtx', 'Evtx']:
    		with open(cwd + '/python_evtx_master/config.yml') as f:
        		doc = yaml.load(f)
		doc['cfevtx'][option] = None
		with open(cwd + '/python_evtx_master/config.yml', 'w') as f:
        		yaml.dump(doc, f)

     def do_execute(self, tool):
	"""Executes the selected tool"""
	if self.context in ['dumpzilla', 'Dumpzilla']:
		dumpzilla()
	elif self.context in ['hindsight', 'Hindsight']:
		hindsight()
	elif self.context in ['evtx', 'Evtx']:
		evtx()

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
	print("Type use <tool> to use a tool or help <tool> to view options for a tool")

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
	print("Type use <tool> to use a tool or help <tool> to view options for a tool")

     def do_evtx(self, args):
	""" Parses .evtx files to XML format """
	print("Type use <tool> to use a tool or help <tool> to view options for a tool")

     def do_exit(self, args):
        """Exits the program"""
        print ("Exiting.")
        raise SystemExit

if __name__ == '__main__':
    prompt = cprompt()
    prompt.prompt = 'aaf>> '
    prompt.cmdloop('''

      ___           ___       _______    .___________.  ______     ______    __       __  ___  __  .___________.
     /   \         /   \     |   ____|   |           | /  __  \   /  __  \  |  |     |  |/  / |  | |           |
    /  ^  \       /  ^  \    |  |__      `---|  |----`|  |  |  | |  |  |  | |  |     |  '  /  |  | `---|  |----`
   /  /_\  \     /  /_\  \   |   __|         |  |     |  |  |  | |  |  |  | |  |     |    <   |  |     |  |     
  /  _____  \   /  _____  \  |  |            |  |     |  `--'  | |  `--'  | |  `----.|  .  \  |  |     |  |     
 /__/     \__\ /__/     \__\ |__|            |__|      \______/   \______/  |_______||__|\__\ |__|     |__|     
                                                                                                                ''')
