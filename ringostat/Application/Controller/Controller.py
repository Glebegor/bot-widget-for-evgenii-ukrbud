from .ManagersController import ManagerController

class Controller:
    def __init__(self, client, db, config):
        self.client = client
        self.db = db
        self.config = config
        print('!! Controller initialized')

    def run(self):
        managerController = ManagerController('/api/v1', self.client, self.db, self.config)
        managerController.run()

