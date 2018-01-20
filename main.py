from requirements import *
from vend import *
from filereader import *


# load products
# product_db = load_db()

# create Vend instance
V = Vend()
print V.get_inventory_counts()

# create counts
# for name, _id in outlets.items():
	# V.create_inventory_count(_id)

# V.delete_consignments()

# V.start_inventory_counts()


# for product in product_db:
# 	_product = {
# 		"id" 		: product["id"],
# 		"inventory" : 
# 	}
# 	V.update_inventory_count_product(_product)



# print V.update_inventory_count_product(product)
print "complete\n"



# read CSV and get inventory data for each product
# compare len(csv data) and len(all products) - find mismatch

# for each location:
	# create inventory count
	# update inventory amount for each product

# report errors 