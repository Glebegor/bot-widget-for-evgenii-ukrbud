import dotenv
import yaml
import os
import sqlite3

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
                'name': configParser['db']['Name'],
                'password': os.getenv('DB_PASSWORD'),
                'admin-password': os.getenv('DB_ADMIN_PASSWORD'),
                'admin-user': configParser['db']['Admin']
            },
            'debug': True,
        }
        print('\n!! Config initialized')


    def ToDict(self):
        return self.config


class Db:
    def __init__(self, config):
        self.config = config
        self.con = sqlite3.connect(config["db"]["name"] + ".db")
        self.cur = self.con.cursor()
        print('!! Database initialized')


