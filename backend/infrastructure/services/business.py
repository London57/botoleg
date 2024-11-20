from application.interfaces.services.business import IBusinessService

from infrastructure.dbs.mongodb.repositories.business import BusinessRepository

class BusinessService(IBusinessService):
	repo = BusinessRepository()

	def get_business_info(self, business_id: int):
		return self.repo.get_business_by_id(business_id)