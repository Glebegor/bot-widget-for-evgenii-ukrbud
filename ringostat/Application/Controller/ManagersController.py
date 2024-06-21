
def NewManagersController(path, client, config, service):
    return ManagerController(path, client, config, service)

class ManagerController:
    def __init__(self, path, client, config, service):
        self.endpoint = '/managers'
        self.path = path + self.endpoint

        self.service = service
        self.client = client
        self.config = config

        print('- ManagerController initialized')

    def run(self):
        @self.client.route(self.path, methods=['GET'])
        def Get():
            return self.service.Get()

        @self.client.route(self.path + "/:id", methods=['GET'])
        def GetById():
            return self.service.GetById()

        @self.client.route(self.path, methods=['POST'])
        def Create():
            return self.service.Create()

        @self.client.route(self.path + "/:id", methods=['PUT'])
        def Update():
            return self.service.Update()

        @self.client.route(self.path + "/:id", methods=['DELETE'])
        def Delete():
            return self.service.Delete()

