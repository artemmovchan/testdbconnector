from models import DBConnector
from env_const import EnvironmentVariables as ev


def send_sql_query_service(data):
    host = ev.get_host()
    dbname = ev.get_db_name()
    driver = ev.get_driver()
    username = ev.get_username()
    password = ev.get_password()
    function = data.get('function')
    if (host is not None and dbname is not None and driver is not None and function is not None and username is not None and password is not None):
        return DBConnector(driver=driver,
                             host=host,
                             dbname=dbname,
                             username=username,
                             password=password).send_sql_query(function=function)
    else:
        raise Exception('Missing parameters')