

class ManagerController:
    def __init__(self, path, client, db, config):
        self.endpoint = '/managers'
        self.path = path + self.endpoint
        self.client = client
        self.db = db
        self.config = config
        print('- ManagerController initialized')

    def run(self):
        @self.client.route(self.path, methods=['GET'])
        def Get():
            return 'Hello, World!'

        @self.client.route(self.path + "/:id", methods=['GET'])
        def GetById():
            return 'Hello, World!'

        @self.client.route(self.path, methods=['POST'])
        def Create():
            return 'Hello, World!'

        @self.client.route(self.path + "/:id", methods=['PUT'])
        def Update():
            return 'Hello, World!'

        @self.client.route(self.path + "/:id", methods=['DELETE'])
        def Delete():
            return 'Hello, World!'

