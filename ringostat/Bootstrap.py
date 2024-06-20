import dotenv
import yaml
import os

class Application:
    def __init__(self, config, db):
        self.config = config
        self.db = db



    def run(self):
        print('-- Application is running')


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
        print('\n!! Config setup')


    def ToDict(self):
        return self.config

class Db:
    def __init__(self, config):
        self.config = config
        print('!! Database setup')

