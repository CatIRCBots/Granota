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

print "\e[1;37mGranota testing script\e[0m\n"

print "\e[0;37mConnecting to IRC...\e[0m"
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect(("irc.lizardirc.org", 6667))
def send(msg):
	message = msg.encode('utf-8') + b'\r\n'
	irc.send(message)
time.sleep(2)
send("NICK GranoTest")
send("USER GranoTest * * :Granota testing bot")
time.sleep(6)
send("JOIN #catbots-bots")
time.sleep(0.5)
print "\e[1;36mGranota testing script has started.\e[0m\n"
send("PRIVMSG #catbots-bots :\x0311Granota testing script has started.\x0F")

print "\e[1;33mTesting\e[0m: Core\n"
send("PRIVMSG #catbots-bots :\x0308Testing\x0F: Core")

print "\e[1;33mTesting\e[0m: willie.__init__"
try:
	import willie.__init__
	print "\e[1;32mWORKING\e[0m: willie.__init__\n"
	working.append("willie.__init__")
except:
	print "\e[0;31mFAILING\e[0m: willie.__init__\n"
	notworking.append("willie.__init__")
	criticalnotworking.append("willie.__init__")

print "\e[1;33mTesting\e[0m: willie.bot"
try:
	import willie.bot
	print "\e[1;32mWORKING\e[0m: willie.bot\n"
	working.append("willie.bot")
except:
	print "\e[0;31mFAILING\e[0m: willie.bot\n"
	notworking.append("willie.bot")
	criticalnotworking.append("willie.bot")

print "\e[1;33mTesting\e[0m: willie.config"
try:
	import willie.config
	print "\e[1;32mWORKING\e[0m: willie.config\n"
	working.append("willie.config")
except:
	print "\e[0;31mFAILING\e[0m: willie.config\n"
	notworking.append("willie.config")
	criticalnotworking.append("willie.config")

print "\e[1;33mTesting\e[0m: willie.irc"
try:
	import willie.irc
	print "\e[1;32mWORKING\e[0m: willie.irc\n"
	working.append("willie.irc")
except:
	print "\e[0;31mFAILING\e[0m: willie.irc\n"
	notworking.append("willie.bot")
	criticalnotworking.append("willie.bot")

print "\e[1;33mTesting\e[0m: willie.tools"
try:
	import willie.tools
	print "\e[1;32mWORKING\e[0m: willie.tools\n"
	working.append("willie.tools")
except:
	print "\e[0;31mFAILING\e[0m: willie.tools\n"
	notworking.append("willie.tools")
	criticalnotworking.append("willie.tools")

print "\n\e[1;33mTesting\e[0m: granota.py"
send("PRIVMSG #catbots-bots :\x0308Testing\x0F: granota.py")
testgra = pytest.main(["granota.py", "-s", '--tb', 'native'])

if testgra is 0:
	print "\e[1;32mWORKING\e[0m: granota.py\n"
	working.append("granota.py")
else:
	print "\e[0;31mFAILING\e[0m: granota.py\n"
	notworking.append("granota.py")
	criticalnotworking.append("granota.py")

print "\e[1;33mTesting\e[0m: Modules\n" 
send("PRIVMSG #catbots-bots :\x0308Testing\x0F: Modules")

for val in os.listdir("willie/modules"):
	if val.find("__init__") == -1 and val.find(".pyc") == -1 and val.find("__pycache__") == -1:
		print "\e[1;33mTesting\e[0m: Module {0}".format(val)
		testmod = pytest.main(["willie/modules/{0}".format(val), "-s", '--tb', 'native'])
		if testmod is 0:
			print "\e[1;32mWORKING\e[0m: Module {0}".format(val)
			working.append("module {0}".format(val))
		else:
			print "\e[0;31mFAILING\e[0m: Module {0}".format(val)
			notworking.append("module {0}".format(val))

print "\nThe tests have been done successfully.\n"

print "============================= \e[1;35mmtest results\e[0m =============================="
send("PRIVMSG #catbots-bots :============================= \x0313test results\x0F ==============================")
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
print "\e[1;32mWORKING\e[0m: {0}{1} in total".format(workingvals, workingnum)
if workingircvals2 is not "": 
	send("PRIVMSG #catbots-bots :\x0309WORKING\x0F: {0}".format(workingircvals1))
	send("PRIVMSG #catbots-bots :{0}{1} in total".format(workingircvals2, workingnum))
else: # wat?
	send("PRIVMSG #catbots-bots :\x0309WORKING\x0F: {0}{1} in total".format(workingircvals1, workingnum))
print "\e[0;31mFAILING\e[0m: {0}{1} in total".format(notworkingvals, notworkingnum)
send("PRIVMSG #catbots-bots :\x0304FAILING\x0F: {0}{1} in total".format(notworkingvals, notworkingnum))
print "\e[0;31mCRITICALLY FAILING\e[0m: {0}{1} in total".format(criticalnotworkingvals, criticalnotworkingnum)
send("PRIVMSG #catbots-bots :\x02\x0304CRITICALLY FAILING\x0F: {0}{1} in total".format(criticalnotworkingvals, criticalnotworkingnum))
if criticalnotworkingnum is 0 and notworkingnum is not 0:
	print "The build has \e[1;32mpassed\e[0m, but there are \e[0;31mfailing\e[0m stuff that should get fixed."
	send("PRIVMSG #catbots-bots :The build has \x0309passed\x0F, but there are \x0304failing\x0F stuff that should get fixed.")
elif criticalnotworkingnum is 0 and notworkingnum is 0:
	print "The build has \e[1;32mpassed\e[0m with no problems."
	send("PRIVMSG #catbots-bots :The build has \x0309passed\x0F with no problems.")
else:
	print "The build has \e[0;31mfailed\e[0m."
	send("PRIVMSG #catbots-bots :The build has \x02\x0304failed\x0F.")
send("PRIVMSG #catbots-bots :For more information please visit https://travis-ci.org/CatIRCBots/Granota")
print "============================= \e[1;35mmtest results\e[0m =============================="
send("PRIVMSG #catbots-bots :============================= \x0313test results\x0F ==============================")
send("QUIT :\x0302My job here, is done!\x0F")
time.sleep(0.3)
if criticalnotworkingnum is 0:
	sys.exit(0)
else:
	sys.exit(1)
