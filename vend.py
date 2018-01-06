from requirements import *

outlets = {
	"Mt Auburn"	: "01f9c6db-e35e-11e2-a415-bc764e10976c",
	"Off Site"	: "060f02b1-c83d-11e7-e913-2c44c86b9c18",
	"Garage"	: "064dce89-c73d-11e5-ec2a-c92ca32c62a3",
	"JFK"		: "605445f3-3846-11e2-b1f5-4040782fde00",
	"Basement"	: "f92e438b-3db4-11e2-b1f5-4040782fde00",
	"Quality"	: "a2ec3422-cb33-11e3-a0f5-b8ca3a64f8f4"
}

class Vend:

	def __init__(self):
		self.headers = {'Authorization' : 'Bearer 2tQzNrcZpJ7vDDXgznMJzk_L7SPCAdXJzyP6FYHA'}
		self.domain_prefix = "harvardshop"

	def update_inventory(self, product_id, inventory):

		url = "https://{}.vendhq.com/api/products".format(self.domain_prefix, product_id)
		
		# assert product exists
		product = requests.get(url + "/" + product_id, headers = self.headers).json()["products"]
		assert len(product) == 1

		payload = {"id": product_id,
    				"inventory": [{
        				"outlet_id": outlets["Basement"],
				        "count": 21
    				}]
		}

		product = requests.post(url, headers = self.headers, params = payload)

		return str(product)