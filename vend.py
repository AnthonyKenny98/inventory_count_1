from requirements import *

outlets = {
	"Mt Auburn"			: "01f9c6db-e35e-11e2-a415-bc764e10976c",
	"Garage"			: "064dce89-c73d-11e5-ec2a-c92ca32c62a3",
	"JFK"				: "605445f3-3846-11e2-b1f5-4040782fde00",
	"Basement"			: "f92e438b-3db4-11e2-b1f5-4040782fde00",
	"Quality Graphics"	: "a2ec3422-cb33-11e3-a0f5-b8ca3a64f8f4"
}

class Vend:

	def __init__(self):
		self.headers = {'Authorization' : 'Bearer 2tQzNrcZpJ7vDDXgznMJzk_L7SPCAdXJzyP6FYHA'}
		self.domain_prefix = "harvardshop"
		self.consignments = []
	
	def get_product(self, product_id):

		# url to get product info
		url = "https://{}.vendhq.com/api/products/{}".format(self.domain_prefix, product_id)
		
		# assert product exists
		product = requests.get(url, headers = self.headers).json()["products"]
		assert len(product) == 1

		return product

	def get_inventory_counts(self, status = "STOCKTAKE_IN_PROGRESS"):
		
		url = "https://{}.vendhq.com/api/2.0/consignments".format(self.domain_prefix)
		
		payload = {
			"type" 		: "STOCKTAKE",
			"status"	: status
		}

		consignments = requests.get(url, headers = self.headers, params = payload).json()["data"]

		self.consignments = []
		for consignment in consignments:
			self.consignments.append(consignment)

	def create_inventory_count(self, outlet):

		# url to create inventory count
		url = "https://{}.vendhq.com/api/2.0/consignments".format(self.domain_prefix)

		payload = {	
			"outlet_id" 	: outlet,
			"name"			: "Test [SCHEDULED]",
			"status"		: "STOCKTAKE_SCHEDULED",
			"type"			: "STOCKTAKE",
			"show_inactive" : 1
		}

		r = requests.post(url, headers = self.headers, data = payload)
		consignment = r.json()["data"]

		self.consignments.append(consignment)
		return r

	# Must be used in same instance as create_inventory_counts
	def start_inventory_counts(self):

		self.get_inventory_counts(status="STOCKTAKE_SCHEDULED")	
		for consignment in self.consignments:
			
			# url to create inventory count
			url = "https://{}.vendhq.com/api/2.0/consignments/{}".format(self.domain_prefix, consignment["id"])

			payload = {
				"outlet_id" : consignment["outlet_id"],
				"name" 		: "Test [IN PROGRESS]",
				"status"	: "STOCKTAKE_IN_PROGRESS",
				"type"		: "STOCKTAKE"
			}

			consignment = requests.put(url, headers = self.headers, data = payload).json()["data"]

	def delete_consignments(self):

		self.get_inventory_counts()

		for consignment in self.consignments:
			url = "https://{}.vendhq.com/api/2.0/consignments/{}".format(self.domain_prefix, consignment)
			requests.delete(url, headers = self.headers)

	def update_inventory_count_product(self, product):

		if len(self.consignments) == 0:
			self.get_inventory_counts()

		consignment = self.consignments[0]

		url = "https://{}.vendhq.com/api/2.0/consignments/{}/products".format(self.domain_prefix, consignment["id"])

		payload = {
			"product_id" 	: product["id"],
			"received"		: product["inventory"]
		}

		return requests.post(url, headers = self.headers, data = payload).text
		