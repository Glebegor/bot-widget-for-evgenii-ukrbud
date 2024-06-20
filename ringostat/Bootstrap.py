import dotenv
import yaml
import os

class Application:
    def __init__(self, config):
        self.config = config

    def run(self):
        print('Application is running')
        print('Config is:', self.config)


class Config:
    def __init__(self):
        dotenv.load_dotenv()
        configParser = yaml.load(open('Config/config.yml'), Loader=yaml.FullLoader)
        self.config = {
            'host': configParser['server']['Host'],
            'port': configParser['server']['Port'],
            'secret-key': os.getenv('SECRET_KEY'),
            'db': {
                'host': configParser['db']['Host'],
                'port': configParser['db']['Port'],
                'name': configParser['db']['Name'],
                'password': os.getenv('DB_PASSWORD'),
                'admin-password': os.getenv('DB_ADMIN_PASSWORD'),
                'admin-user': configParser['db']['Admin']
            },
            'debug': True,
        }

    def ToDict(self):
        return self.config