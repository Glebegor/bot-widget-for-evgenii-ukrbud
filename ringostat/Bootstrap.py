import dotenv

class Application:
    def __init__(self, config):
        self.config = config

    def run(self):
        print('Application is running')
        print('Config is:', self.config)


class Config:
    def __init__(self):
        dotenv.load_dotenv()
        self.config = {
            'host': 'localhost',
            'port': 8080,
            'secret-key': os.getenv('SECRET_KEY'),
            'db': {
                'host': 'localhost',
                'port': 5436,
                'name': 'ringostat',
                'password': os.getenv('DB_PASSWORD'),
                'admin-password': os.getenv('DB_ADMIN_PASSWORD'),
                'admin-user': 'admin'
            },
            'debug': True,
        }

    def ToDict(self):
        return self.config