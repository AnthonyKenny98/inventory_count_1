from requirements import *
from effects import *

def load_db(filepath):

	product_db = []

	# set up file and csv readers
	try:
		file = open(filepath, 'r')
		rows = csv.reader(file, delimiter = ',', quotechar = '|')
		csv_len = len(file.readlines())
	except:
		printFilePathError(filepath, "load")
		return product_db

	# set up progress bar
	bar = ProgressBar(maxval=csv_len, term_width=40, widgets=[Percentage(), Bar()])
	bar.start()
	
	file.seek(0)
	next(rows)
	for row in rows:

		product = {
			"id" 		: row[0],
			"handle"	: row[1],
			"sku" 		: row[2],
			"name" 		: row[3],
			"var1 name" : row[4],
			"var1 val"	: row[5],
			"var2 name" : row[6],
			"var2 val"	: row[7],
			"var3 name" : row[8],
			"var3 val"	: row[9],
			"supplier"	: row[10],
			"active" 	: row[11],
			"Basement"	: row[12],
			"Garage"	: row[13],
			"JFK"		: row[14],
			"Mt Auburn" : row[15],
			"Quality Graphics"	: row[16]	
		}

		product_db.append(product)

		bar.update()
	bar.finish()


	if csv_len - len(product_db) != 1:
		printWarningGeneral("product data len does not match input csv ({})".format(csv_len))
	return product_db