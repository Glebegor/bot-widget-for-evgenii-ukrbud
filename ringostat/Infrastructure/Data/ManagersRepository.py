from ..Service.ManagersService import ManagersService

def NewManagersRepository(db):
    return ManagersService(db)
class ManagersRepository:
    def __init__(self, db):
        self.db = db

    def Get(self):
        return 'QUERY GET'

    def GetById(self, id):
        return 'QUERY GET id'

    def Create(self, data):
        return 'QUERY CREATE'

    def Update(self, id, data):
        return 'QUERY UPDATE'

    def Delete(self, id):
        return 'QUERY DELETE'