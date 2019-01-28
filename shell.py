from cmd import Cmd
from vend import *
from effects import *
from filereader import *

class MyPrompt(Cmd):

    def do_show(self, args):
    	"""\nShows selected data.\nArgs: \n   counts [scheduled / in_progress]n   product_data\n"""
    	
    	V.get_inventory_counts()
    	if args == "counts":
    		print(V.scheduled_consignments + V.progress_consignments)
    	elif args == "counts scheduled":
    		print(V.scheduled_consignments)
    	elif args == "counts in_progress":
    		print(V.progress_consignments)
    	elif args == "product_data":
    		print(product_db)
    	else:
    		printInputError("show")

    def do_length(self, args):
    	"""\nLength of selected data.\nArgs:\n   counts [scheduled / in_progress]n   product_data\n"""

    	V.get_inventory_counts()
    	if args == "counts":
    		print(len(V.scheduled_consignments) + len(V.progress_consignments))
    	elif args == "counts scheduled":
    		print(len(V.scheduled_consignments))
    	elif args == "counts in_progress":
    		print(len(V.progress_consignments))
    	elif args == "product_data":
    		print(len(product_db))
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
            name = input("\n Please provide name for inventory count: ")
            print(V.create_inventory_count(outlets[args], name).text)
        else:
            printInputError("create_count")

    def do_start_counts(self, args):
    	""" \nChanges all scheduled counts status to IN PROGRESS"""
    	V.start_inventory_counts()

    def do_product_count(self, args):
        """\nAdds product data to relevant count\nArgs: \n   <outlet>"""
    	
        if len(args) == 0 or args not in outlets.keys():
            printInputError("product_count")
        else:

            outlet_id = outlets[args]

            V.get_inventory_counts()
	    	
            count = None
            for consignment in V.progress_consignments:
                if consignment["outlet_id"] == outlet_id:
                    count = consignment
                    break

            if not count:
                print("Aborted: No counts in progress for outlet: {}".format(args))
                return

            print("Count Name: " + count["name"])
            print("Count Outlet: " + args)

            proceed = input("\nReady to proceed with this count? (y/n): ")

            if len(product_db) == 0:
                print("Aborted: product_db empty")
                return

            if proceed != "y":
                print("aborted")
                return

            print("Updating Inventory Count")
            errors = []

	    	# status bar
            bar = ProgressBar(maxval=len(product_db), term_width=40, widgets=[Percentage(), Bar(), Counter()])
            bar.start()

            for i in range(len(product_db)):
                try:
                    r = V.update_inventory_count_product(count["id"], product_db[i]["id"], product_db[i][args])
                    if r.status_code != 201:
                        errors.append(product_db[i])
                    bar.update(i)
                except:
                    errors.append(product_db[i])
                    print("retrying on {}".format(i))
                    i -= 1
            bar.finish()
            print("Complete with {} errors".format(len(errors)))



    def do_outlets(self, args):
    	"""\nLists all Outlets\nArgs: NULL"""
    	print(str(outlets.keys()))

    def do_clear(self, args):
    	"""\nClears the UI. Does not wipe data. \nArgs: NULL\n"""
    	clear()
    	shell_intro()

    def do_quit(self, args):
        """\nQuits the program.\n"""
        print("Quitting.")
        time.sleep(1)
        clear()
        raise SystemExit


if __name__ == '__main__':

	V = Vend()
	product_db = []

	shell_intro()
	connection_intro()
	prompt = MyPrompt()
	prompt.prompt = '> '
	prompt.cmdloop()

