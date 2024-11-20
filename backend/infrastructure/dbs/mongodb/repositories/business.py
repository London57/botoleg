from application.interfaces.repositories.business import IBusinessRepository

from infrastructure.dbs.mongodb.options.db import businesses_collection


class BusinessRepository(IBusinessRepository):
	collection = businesses_collection

	def get_business_by_id(self, business_id: int) -> dict:
		import time
		t1 = time.time()
		res = self.collection.find_one({"business_id": business_id})
		print(res)
		print(time.time() - t1)
		return res
	
	def update_business(self, business_id, update_data: dict) -> None:
		self.collection.update_one({"business_id": business_id}, {"$set": update_data})