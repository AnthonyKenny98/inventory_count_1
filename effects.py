import time
import sys
import os
from requirements import *

def shell_intro():
	clear()
	print"\n"
	print "The Harvard Shop"
	print "Inventory Count 2018"
	print "\n"
	print "### Data Upload Interface ###"
	print "=============================\n"

def connection_intro():
	print "\n\n"
	time.sleep(3)
	print "Establishing connection to Vend"

	time.sleep(0.5)
	print "............"
	time.sleep(0.5)
	print "............"
	time.sleep(0.5)
	print "\n\nFirewall encountered...."
	time.sleep(2)
	bar = ProgressBar(maxval=100, term_width=50, widgets=[Percentage(), Bar()])
	bar.start()
	for i in range(100):
		time.sleep(0.05)
		bar.update(i)
	bar.finish()
	print "All credentials passed"

	print "............"
	time.sleep(0.5)
	print "............"
	time.sleep(0.5)

	print "Connection Established\n"

def clear():
	os.system('clear')

# ERROR MESSAGES
def printInputError(msg = ""): 
	print "\n==================================================="
	print "Input Error: incorrect/incomplete arguments provided"
	print "(For help type 'help {}')\n".format(msg)

def printFilePathError(msg1 = "", msg2 = ""):
	print "\n==================================================="
	print "File Path Error: filepath '{}' is invalid, please try again".format(msg1)
	print "(For help type 'help {}')\n".format(msg2)

def printWarningGeneral(msg):
	print "\n==================================================="
	print "Warning: {}".format(msg)
