from ..Service.ManagersService import ManagersService

def NewManagersRepository(db):
    return ManagersService(db)
class ManagersRepository:
    def __init__(self, db):
        self.db = db