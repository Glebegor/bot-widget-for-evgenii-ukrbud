

def NewManagersService(repo):
    return ManagersService(repo)
class ManagersService:
    def __init__(self, repo):
        self.repo = repo

    def Get(self):
        return 'Hello, World! Get'

    def GetById(self, id):
        return 'Hello, World! Get id'

    def Create(self, data):
        return 'Hello, World! Create'

    def Update(self, id, data):
        return 'Hello, World! Update'

    def Delete(self, id):
        return 'Hello, World! Delete'
