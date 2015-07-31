# coding=utf-8
"""
Granota testing script

Tests Granota's script searching possible bugs. 

NOTE: This is supposed to be used on Travis CI.
"""

import sys
import os
import pytest
import socket
import time

working = []
notworking = []
criticalnotworking = []

print "Granota testing script\n"

print "Connecting to IRC..."
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect(("irc.lizardirc.org", 6667))
def send(msg):
	message = msg.encode('utf-8') + b'\r\n'
	irc.send(message)
time.sleep(2)
send("NICK GranoTest")
send("USER GranoTest * * :Granota testing bot")
time.sleep(5.5)
send("JOIN #catbots-bots")
send("PRIVMSG #catbots-bots :Granota testing script has started.")
time.sleep(0.5)
print "Done, starting tests.\n"

print "Testing: Core\n"

print "Testing: willie.__init__"
try:
	import willie.__init__
	print "WORKED: willie.__init__\n"
	working.append("willie.__init__")
except:
	print "FAILED: willie.__init__\n"
	notworking.append("willie.__init__")
	criticalnotworking.append("willie.__init__")

print "Testing: willie.bot"
try:
	import willie.bot
	print "WORKED: willie.bot\n"
	working.append("willie.bot")
except:
	print "FAILED: willie.bot\n"
	notworking.append("willie.bot")
	criticalnotworking.append("willie.bot")

print "Testing: willie.config"
try:
	import willie.config
	print "WORKED: willie.config\n"
	working.append("willie.config")
except:
	print "FAILED: willie.config\n"
	notworking.append("willie.config")
	criticalnotworking.append("willie.config")

print "Testing: willie.irc"
try:
	import willie.irc
	print "WORKED: willie.irc\n"
	working.append("willie.irc")
except:
	print "FAILED: willie.irc\n"
	notworking.append("willie.bot")
	criticalnotworking.append("willie.bot")

print "Testing: willie.tools"
try:
	import willie.tools
	print "WORKED: willie.tools\n"
	working.append("willie.tools")
except:
	print "FAILED: willie.tools\n"
	notworking.append("willie.tools")
	criticalnotworking.append("willie.tools")

print "\nTesting: granota.py"
testgra = pytest.main(["granota.py", "-s", '--tb', 'native'])

if testgra is 0:
	print "WORKED: granota.py\n"
	working.append("granota.py")
else:
	print "FAILED: granota.py\n"
	notworking.append("granota.py")
	criticalnotworking.append("granota.py")

print "SECONDARY TEST: Modules\n" 

for val in os.listdir("willie/modules"):
	if val.find("__init__") == -1 and val.find(".pyc") == -1 and val.find("__pycache__") == -1:
		testmod = pytest.main(["willie/modules/{0}".format(val), "-s", '--tb', 'native'])
		if testmod is 0:
			print "WORKED: Module {0}".format(val)
			working.append("module {0}".format(val))
		else:
			print "FAILED: Module {0}".format(val)
			notworking.append("module {0}".format(val))

print "\nThe tests have been done successfully.\n"

time.sleep(0.5)

print "============================= test results =============================="
send("PRIVMSG #catbots-bots :============================= test results ==============================")
workingnum = len(working)
notworkingnum = len(notworking)
criticalnotworkingnum = len(criticalnotworking)
alltestsmade = workingnum + notworkingnum + criticalnotworkingnum
workingvals = ""
workingircvals1 = "" # due to the lengh is too long, we do this
workingircvals2 = "" # ^
notworkingvals = ""
criticalnotworkingvals = ""
for val in working:
	workingvals = workingvals + val + ", "
	if len(workingircvals1) > 400: ## just an protection
		workingircvals2 = workingircvals2 + val + ", "
	else:
		workingircvals1 = workingircvals1 + val + ", "
for val in notworking:
	notworkingvals = notworkingvals + val + ", "
for val in criticalnotworking:
	criticalnotworkingvals = criticalnotworkingvals + val + ", "
print "Tests made: {0}".format(alltestsmade)
send("PRIVMSG #catbots-bots :Tests made: {0}".format(alltestsmade))
print "Working: {0}{1} in total".format(workingvals, workingnum)
if workingircvals2 is not "": 
	send("PRIVMSG #catbots-bots :Working: {0}".format(workingircvals1))
	send("PRIVMSG #catbots-bots :{0}{1} in total".format(workingircvals2, workingnum))
else: # wat?
	send("PRIVMSG #catbots-bots :Working: {0}{1} in total".format(workingircvals1, workingnum))
print "Not working: {0}{1} in total".format(notworkingvals, notworkingnum)
send("PRIVMSG #catbots-bots :Not working: {0}{1} in total".format(notworkingvals, notworkingnum))
print "CRITICAL not working: {0}{1} in total".format(criticalnotworkingvals, criticalnotworkingnum)
send("PRIVMSG #catbots-bots :CRITICAL not working: {0}{1} in total".format(criticalnotworkingvals, criticalnotworkingnum))
if criticalnotworkingnum is 0 and notworkingnum is not 0:
	print "The build has passed, but there are not working stuff that should get fixed."
	send("PRIVMSG #catbots-bots :The build has passed, but there are not working stuff that should get fixed.")
elif criticalnotworkingnum is 0 and notworkingnum is 0:
	print "The build has passed with no problems."
	send("PRIVMSG #catbots-bots :The build has passed with no problems.")
else:
	print "The build has failed."
	send("PRIVMSG #catbots-bots :The build has failed.")
send("PRIVMSG #catbots-bots :For more information please visit https://travis-ci.org/CatIRCBots/Granota")
print "============================= test results =============================="
send("PRIVMSG #catbots-bots :============================= test results ==============================")
send("QUIT :My job here, is done!")
time.sleep(0.3)
if criticalnotworkingnum is 0:
	sys.exit(0)
else:
	sys.exit(1)
