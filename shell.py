from cmd import Cmd
from vend import *
from effects import *
from filereader import *

class MyPrompt(Cmd):

    def do_show(self, args):
    	"""\nShows selected data.\nArgs: \n   vend consignments\n   product data\n"""
    	
    	if args == "vend consignments":
    		V.get_inventory_counts()
    		print V.consignments
    	elif args == "product data":
    		print str(product_db)
    	else:
    		printInputError("show")

    def do_length(self, args):
    	"""\nLength of selected data.\nArgs:\n   vend consignments\n   product data\n"""

    	if args == "vend consignments":
    		V.get_inventory_counts(status="STOCKTAKE_SCHEDULED")
    		print len(V.consignments)
    	elif args == "product data":
    		print len(product_db)
    	else:
    		printInputError("length")

    def do_load(self, args):
        """\nLoads data from CSV.\nArgs: <filepath>\n"""
        
        if len(args) > 0:
        	global product_db
        	product_db = load_db(args)
        else:
            printInputError("load")

    def do_create_count(self, args):
    	"""\nCreates Inventory Count in Vend\nArgs:\n   <outlet name>"""
    	
    	if args in outlets.keys():
        	print V.create_inventory_count(outlets[args])
        else:
        	printInputError("create_count")

    def do_start_counts(self, args):
    	""" \nChanges all scheduled counts status to IN PROGRESS"""
    	V.start_inventory_counts()

    def do_outlets(self, args):
    	"""\nLists all Outlets\nArgs: NULL"""
    	print str(outlets.keys())

    def do_clear(self, args):
    	"""\nClears the UI. Does not wipe data. \nArgs: NULL\n"""
    	clear()
    	shell_intro()

    def do_quit(self, args):
        """\nQuits the program.\n"""
        print "Quitting."
        time.sleep(1)
        clear()
        raise SystemExit


if __name__ == '__main__':

	V = Vend()
	product_db = []

	shell_intro()
	# connection_intro()
	prompt = MyPrompt()
	prompt.prompt = '> '
	prompt.cmdloop()

