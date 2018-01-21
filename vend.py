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
		self.scheduled_consignments = []
		self.progress_consignments = []
	
	def get_product(self, product_id):

		# url to get product info
		url = "https://{}.vendhq.com/api/products/{}".format(self.domain_prefix, product_id)
		
		# assert product exists
		product = requests.get(url, headers = self.headers).json()["products"]
		assert len(product) == 1

		return product

	def get_inventory_counts(self):
		
		self.scheduled_consignments = []
		self.progress_consignments = []

		url = "https://{}.vendhq.com/api/2.0/consignments".format(self.domain_prefix)
		
		payload = {
			"type" 		: "STOCKTAKE",
			"status"	: "STOCKTAKE_SCHEDULED"
		}
		self.scheduled_consignments = requests.get(url, headers = self.headers, params = payload).json()["data"]

		payload["status"] = "STOCKTAKE_IN_PROGRESS"
		self.progress_consignments = requests.get(url, headers = self.headers, params = payload).json()["data"]

	def create_inventory_count(self, outlet, name):

		# url to create inventory count
		url = "https://{}.vendhq.com/api/2.0/consignments".format(self.domain_prefix)

		payload = {	
			"outlet_id" 	: outlet,
			"name"			: name,
			"status"		: "STOCKTAKE_SCHEDULED",
			"type"			: "STOCKTAKE",
			"show_inactive" : 1
		}

		r = requests.post(url, headers = self.headers, data = payload)
		self.get_inventory_counts()
		return r

	# Must be used in same instance as create_inventory_counts
	def start_inventory_counts(self):

		self.get_inventory_counts()	
		for consignment in self.scheduled_consignments:
			
			# url to create inventory count
			url = "https://{}.vendhq.com/api/2.0/consignments/{}".format(self.domain_prefix, consignment["id"])

			payload = {
				"outlet_id" : consignment["outlet_id"],
				"name" 		: consignment["name"],
				"status"	: "STOCKTAKE_IN_PROGRESS",
				"type"		: "STOCKTAKE"
			}

			requests.put(url, headers = self.headers, data = payload)
			self.get_inventory_counts()

	def delete_consignments(self):

		self.get_inventory_counts()

		for consignment in self.scheduled_consignments:
			url = "https://{}.vendhq.com/api/2.0/consignments/{}".format(self.domain_prefix, consignment)
			requests.delete(url, headers = self.headers)
		self.get_inventory_counts()

	def update_inventory_count_product(self, count_id, product_id, inventory):

		url = "https://{}.vendhq.com/api/2.0/consignments/{}/products".format(self.domain_prefix, count_id)

		payload = {
			"product_id" 	: product_id,
			"received"		: inventory
		}

		return requests.post(url, headers = self.headers, data = payload)
		