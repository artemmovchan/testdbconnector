from dotenv import load_dotenv
import os

load_dotenv()

class EnvironmentVariables:
    _HOST = os.environ.get('HOST')
    _DB_NAME = os.environ.get('DB_NAME')
    _DRIVER = os.environ.get('DRIVER')
    _USERNAME = os.environ.get('USERNAME')
    _PASSWORD = os.environ.get('PASSWORD')
    
    @classmethod
    def get_host(cls):
        return cls._HOST
    
    @classmethod
    def get_db_name(cls):
        return cls._DB_NAME
    
    @classmethod
    def get_driver(cls):
        return cls._DRIVER
    
    @classmethod
    def get_username(cls):
        return cls._USERNAME
    
    @classmethod
    def get_password(cls):
        return cls._PASSWORD
    
    