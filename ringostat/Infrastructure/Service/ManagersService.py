

def NewManagersService(repo):
    return ManagersService(repo)
class ManagersService:
    def __init__(self, repo):
        self.repo = repo
