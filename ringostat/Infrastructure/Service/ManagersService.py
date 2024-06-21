

def NewManagersService(repo):
    return ManagersService(repo)
class ManagersService:
    def __init__(self, repo):
        self.repo = repo

    def Get(self):
        print(self.repo)
        return self.repo.Get()

    def GetById(self, id):
        return self.repo.GetById(id)

    def Create(self, data):
        return self.repo.Create(data)

    def Update(self, id, data):
        return self.repo.Update(id, data)

    def Delete(self, id):
        return self.repo.Delete(id)
