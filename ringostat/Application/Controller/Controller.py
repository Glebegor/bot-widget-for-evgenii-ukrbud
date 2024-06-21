

class Controller:
    def __init__(self, client, db, config):
        self.client = client
        self.db = db
        self.config = config
        print('!! Controller initialized')

    def run(self):
        @self.client.route('/api/v1')
        def index():
            return 'Hello, World!'

        print('!! Controller is running')
